import sys
import bitcoin
import os

import bitcoin.rpc
from bitcoin.core import *
from bitcoin.core.script import *
from bitcoin.wallet import *

#assuming the regtest server is launch:
#bitcoind -regtest -daemon -print

#trying to make a transaction to my address

# 111 = 0x6F = version prefix for Testnet Addresses

bitcoin.SelectParams('regtest')


proxy = bitcoin.rpc.Proxy()

privkey = CBitcoinSecret.from_secret_bytes( os.urandom(32))

print( privkey )
CBitcoinSecret

