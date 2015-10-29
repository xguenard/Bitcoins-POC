import sys

import bitcoin

# basics

secret = bitcoin.random_key()
public = bitcoin.privtopub(secret)

print( "secret : " + secret )
print( "public : " + secret )

# multisig test

pub = []

for x in range( 0 , 3 ):
    rand_sc_key = bitcoin.random_key()
    pub.append( bitcoin.privtopub( rand_sc_key ) )

print( "\n".join(pub) )

script = bitcoin.mk_multisig_script( pub[0] , pub[1] , pub[2] , 2 , 3 )
address = bitcoin.scriptaddr(script)

print( "Script : " + script )
print( "Address : " + address )

try:
    history = bitcoin.unspent( address )
    print( history )
except Exception as msg:
    print( msg  )

