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



class Message():
    def __init__(self, path, tx_msg_size):
        self.path = path
        self.packets = []
        self.msg_size = tx_msg_size

    def FillPackets(self):
        """Fill the packets list with strings of size msg_size"""
        reader = open( self.path , "r")
        tmp = reader.readlines()
        buff = ""
        place = self.msg_size

        for s in tmp:
            if( len(s) >=  place ):
                buff += s[0:place]
                place = 0 
            else :
                buff += s
                place -= len(s)
            if( place == 0):
                self.packets.append(buff)
                buff = ""
                place = self.msg_size


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
