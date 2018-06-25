import unittest
from graphenebase.base58 import Base58
from graphenebase.account import BrainKey, Address, PublicKey, PrivateKey, PasswordKey


class Testcases(unittest.TestCase) :

    # def test_Adress(self):
    #     self.assertEqual([format(Address("ONEFN9r6VYzBK8EKtMewfNbfiGCr56pHDBFi"), "ONE"),
    #                       format(Address("ONEdXrrTXimLb6TEt3nHnePwFmBT6Cck112"), "ONE"),
    #                       format(Address("ONEJQUAt4gz4civ8gSs5srTK4r82F7HvpChk"), "ONE"),
    #                       format(Address("ONEFPXXHXXGbyTBwdKoJaAPXRnhFNtTRS4EL"), "ONE"),
    #                       format(Address("ONE3qXyZnjJneeAddgNDYNYXbF7ARZrRv5dr"), "ONE"),
    #                       ],
    #                      ["ONEFN9r6VYzBK8EKtMewfNbfiGCr56pHDBFi",
    #                       "ONEdXrrTXimLb6TEt3nHnePwFmBT6Cck112",
    #                       "ONEJQUAt4gz4civ8gSs5srTK4r82F7HvpChk",
    #                       "ONEFPXXHXXGbyTBwdKoJaAPXRnhFNtTRS4EL",
    #                       "ONE3qXyZnjJneeAddgNDYNYXbF7ARZrRv5dr",
    #                       ])


    def test_Adress(self):
        address1 = format(PrivateKey("5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3").address, "ONE")

        address2 = format(PublicKey("ONE6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV", prefix="ONE").address, "ONE")

        tempAddress = format(Address("BTSFN9r6VYzBK8EKtMewfNbfiGCr56pHDBFi", prefix="BTS"), "BTS")
        tempAddress = format(Address("ONEFAbAx7yuxt725qSZvfwWqkdCwp9ZnUama", prefix="ONE"), "ONE")

        result = address2 == tempAddress

        ret = 0
