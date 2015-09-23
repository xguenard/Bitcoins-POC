import sys
import bitcoin.rpc
from bitcoin.core import *
from bitcoin.core.script import *
from bitcoin.wallet import *
import os
import binascii

class TestUser():
    def __init__(self):
        self.priv = CBitcoinSecret("cMmTfPasFywvveTqsMEmc2FSqWSLyJVdGYoRgc7c8MvX57rZRLhR")

    def set_addresses(self):
        self.address = "test"



    def print_key(self):
        print( b2x(self.priv.pub) )
        print( self.priv.is_compressed)


   




def main():
    bitcoin.SelectParams('regtest')

    print("Preparing to connect to regtest")

    try:
        proxy = bitcoin.rpc.Proxy()
    except:
        print("Failed connecting to RPC proxy")

    print("\tConnected to rpc proxy")


main()
x = TestUser()
x.print_key()
x.set_addresses()
