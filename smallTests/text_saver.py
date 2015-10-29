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
        buff = ""
        buff_free_space = self.msg_size

        reader = open( self.path , "r")
        for s in reader:
            str_len = len(s)
            ed = len(s)
            if( buff_free_space > str_len ):
                buff += s
                buff_free_space -= str_len
            else:
                pos = 0
                pos1 = 0
                while str_len > 0:
                    pos1 = min( pos + buff_free_space , ed )
                    #print(" pos : " + str(pos) + " , pos1 : " + str(pos1) )
                    buff += s[pos : pos1 ]
                    buff_free_space -= pos1 - pos
                    str_len -= pos1 -pos 
                    pos = pos1
                    
                    if( buff_free_space == 0 ):
                        self.packets.append( buff )
                        buff = ""
                        buff_free_space = self.msg_size
        reader.close()

    def Rebuild(self):
        output = ""
        for s in self.packets:
            output += s
        print( output )


           


    def Print_all(self):
        i = 0
        for s in self.packets:
            print( str(i)+ " : "  + s )
            i += 1


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


m = Message("test.txt" , 30 )
m.FillPackets()
m.Print_all()

print(" ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; ")
m.Rebuild()
