import socket
import sys

HOST = '' 
PORT = 8888

s = socket.socket( socket.AF_INET , socket.SOCK_STREAM )

#Binding : bind a socket to a particular address and port

try:
    s.bind( (HOST, PORT ))
except socket.error as msg:
    print("Binding failed")
    sys.exit()
print( "Socket Binding Complete")


#listen, socket listen to connection.
s.listen(5)
print("Socket  now Listening")

#Accept connection

conn , addr = s.accept()

print( "Connected with " + addr[0] + " : " + str( addr[1] ) )


#talking with the client
data = conn.recv(1024)
conn.sendall( data )

conn.close()
s.close()
