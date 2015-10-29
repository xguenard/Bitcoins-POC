import socket
import sys


host = ''
port = 5000


s = socket.socket( socket.AF_INET , socket.SOCK_STREAM )
s.bind(( host, port ))

s.listen(5)


while 1 :
    conn, addr = s.accept()
    print( "Connected with " + addr[0] + " : " + str( addr[1] ) )

    data = conn.recv( 1024 )
    reply = "Ok ..." + data
    if not data :
        break

    conn.sendall( reply )

conn.close()
s.close()
