import socket
import sys # for exit

try:
    s = socket.socket( socket.AF_INET , socket.SOCK_STREAM)
except socket.error as msg:
    print("failed to create socket")
    sys.exit()

print("Socket Created")
#AF_INET = adress family => here IPv4( IP version 4 )
#SOCK_STREAM = TCP ( stream oriented, .. ?)

print("Socket Created")

#connection = IP address and port number

#how to get Ip of a website?
host = 'www.google.com'
port = 80

try:
    remote_ip = socket.gethostbyname( host )
except socket.gaierror:
    print("Hostname could not be resolved")
    sys.exit()

print( "IP address of " + host + " is " + remote_ip )
#connect to the remote server
s.connect(( remote_ip , port ))

print( 'Socket Connected to ' + host + ' on ip ' + remote_ip)
#Connection concept is proper to TCP
# UDP, ICMP , ARP don't have this concept


#Now sending data
message = b"Happy"

try :
    s.sendall( message)
except socket.error:
    print("Send failed")
    sys.exit()
print("Message send successfully")

#Now receiving data

reply = s.recv(4096)

print( reply )


#Close socket
s.close()
