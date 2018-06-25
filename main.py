#!/usr/bin/env python
# -*- coding:utf-8 -*
import getpass
import json
import sys
import random
import time

from common import globalvar as gl, one_encrypt
from grapheneexchange import GrapheneExchange
import config as file_config
from logs.log import logger


class Config():
    #: Witness connection parameter
    witness_url = file_config.witness_url
    witness_user = file_config.witness_user
    witness_password = file_config.witness_password

    #: The account used here
    account = file_config.account
    wif = file_config.wif

    #: Markets to watch.
    watch_markets = file_config.watch_markets
    market_separator = file_config.market_separator


def connect_client(config):
    return GrapheneExchange(config, safe_mode=False)


def check_balance(client, symbol, total):
    bal = client.returnBalances()
    if bal[symbol] < total:
        return False
    return True


def get_ticker(client):
    return client.returnTicker()


def order_buy(client, market, sell_min, buy_max):
    middle_price = round(random.uniform(sell_min, buy_max), file_config.price_point)
    final_vol = round(random.uniform(file_config.vol_min, file_config.vol_max), file_config.vol_point)
    total = middle_price * final_vol
    symbol = market.split(file_config.market_separator)[0]
    if check_balance(client, symbol, total):
        return client.buy(market, middle_price, final_vol)
    return False


def order_sell(client, market, sell_min, buy_max):
    middle_price = round(random.uniform(sell_min, buy_max), file_config.price_point)
    final_vol = round(random.uniform(file_config.vol_min, file_config.vol_max), file_config.vol_point)
    total = middle_price * final_vol
    symbol = market.split(file_config.market_separator)[0]
    if check_balance(client, symbol, total):
        return client.sell(market, middle_price, final_vol)
    return False


if __name__ == '__main__':
    try:
        input = getpass.getpass('please input password:')
        key = input.strip()
        if key != one_encrypt.decrypt(file_config.ENCRYPT_KEY, key).strip():
            print('password error')
            sys.exit(0)

        gl._init()
        gl.set_value('wif', one_encrypt.decrypt(file_config.wif, key).strip())
    except Exception as e:
        print('encrypt text error')
        sys.exit(0)

    config = Config()
    config.wif = gl.get_value('wif')
    client = connect_client(config)

    counter = 0

    while True:
        try:
            res_tickers = get_ticker(connect_client(config))
            print(res_tickers)
            for key_ticker in res_tickers:
                val_ticker = res_tickers[key_ticker]
                sell_min = val_ticker['lowestAsk']
                buy_max = val_ticker['highestBid']
                # if sell_min<file_config.confirm_min

                if file_config.price_max and file_config.price_min:
                    res_buy = order_buy(client, key_ticker, file_config.price_min, file_config.price_max)
                    res_sell = order_sell(client, key_ticker, file_config.price_min, file_config.price_max)
                else:
                    check_price = round(random.uniform(sell_min, buy_max), file_config.price_point)
                    if check_price<file_config.confirm_min or check_price>file_config.confirm_max:
                        logger.warning('The current price {} exceeds the threshold, please check the configuration.'.format(check_price))
                        continue
                    res_sell = order_sell(client, key_ticker, sell_min, buy_max)
                    res_buy = order_buy(client, key_ticker, sell_min, buy_max)
                if res_buy is False:
                    s_buy = key_ticker.split(file_config.market_separator)[1]
                    logger.warning('Insufficient account balance : {}'.format(s_buy))
                else:
                    logger.info(json.dumps(res_buy))
                if res_sell is False:
                    s_sell = key_ticker.split(file_config.market_separator)[0]
                    logger.warning('Insufficient account balance : {}'.format(s_sell))
                else:
                    logger.info(json.dumps(res_sell))
        except Exception as err:
            logger.error(err)

        time.sleep(file_config.sleep_time)
        counter += 1

        if file_config.count and file_config.count <= counter:
            break
