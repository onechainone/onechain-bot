#!/usr/bin/env python
# -*- coding:utf-8 -*

# 备用节点, 如果默认的这个节点连接不稳定,可以切换到下面这个节点.
# 120.220.14.93:21203
witness_url = "ws://120.220.14.89:21203"
witness_user = ""
witness_password = ""

#: The account used here
account = "onxxxx21"  # 你的账户名
# 加密的账户私钥
wif = '你的加密私钥'

#: Markets to watch.
# 交易对推荐一个程序一个交易对,理论上可以设置多个,但是设置的数量值是一个,会影响逻辑.所以最好只设置一个
watch_markets = ["ONE_ATOMETH"]
market_separator = "_"

# 程序启动秘钥 解密之后是123456
ENCRYPT_KEY = b'\xf6\xb7W\xc5\x91F<\xc8\xec\x82,\xd7\xe9\xd2by'

sleep_time = 1*60  # (seconds) 每一次买单卖单中间间隔的时间
count = None  # 默认是None 是不设置挂单次数,如果设置了就会只执行这个次数

price_point = 8  # 价格的精度值设置,这个在启动程序的时候应该设置一下
vol_point = 8  # 数量的精度值设置,这个在启动程序的时候应该设置一下

# 挂单是买卖数量的区间设置
vol_min = 1
vol_max = 3

# 挂单的价格设置, 默认是None,这样会执行ticker给出的价格区间,否则会按照设置的价格区间走
price_min = None
price_max = None

# 防止ticker获取到的价格区间太小设置的阈值,这个在启动程序时候应该设置, 设置的方式推荐参考当时买卖的最高价和最低价.
confirm_min = 2.5739999997876272e-05
confirm_max = 2.8000000000000003e-05

