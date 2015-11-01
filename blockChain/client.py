import socket

class Client():
    def __init__(self, id_ , name , target):
        self.id_ = id_
        self.name = name
        self.target = target
        self.createSocket()

    def createSocket(self):
        self.sock = socket.socket( socket.AF_INET , socket.SOCK_STREAM )
        self.port = 7004
        self.sock.connect( ( self.target, self.port ) )
        self.sock.send( self.name.encode("utf-8"))

    def SendMsg(self, msg ):
        self.sock.send( msg.encode("utf-8"))
