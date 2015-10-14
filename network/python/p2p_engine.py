import socket
import threading
from PySide import QtGui
import sys

#Goal = create a simple p2p protocol.
#This will be used as a basis for ledging and broker apps

class Server(threading.Thread):
    def __init__(self, id_ , name ):
        super().__init__()
        self.id_ = id_
        self.name = name
        self.CreateSockets()
        self.connections_list = []

    def CreateSockets(self):
        self.sock = socket.socket( socket.AF_INET , socket.SOCK_STREAM )
        self.host = ''
        self.port = 7004 
        self.sock.bind( (self.host , self.port) )
        self.sock.listen(10)
        print( self.host )
        print( self.port )

    def run(self):
        self.Listening()

    def Listening(self):
        while True:
            print("waiting for connections")
            connection , addr  = self.sock.accept()
            print(" connected with : " + addr[ 0] + " : " + str( addr[1] ) )
            self.connections_list.append( SConnection( addr , connection ))
            self.ManageConnection()
        self.sock.close()

    def ManageConnection(self):
        for con in self.connections_list :
            con.start()

class SConnection(threading.Thread):
    def __init__(self, addr , connection ):
        super().__init__()
        self.addr = addr
        self.connection = connection
        self.data = []
        self.size_max = 20

    def run(self):
        self.ReceiveData()

    def ReceiveData(self):
        while True:
            tmp_data = self.connection.recv(4096).decode("utf-8")
            self.AddToData( tmp_data)
            #print( self.data )

    def AddToData(self, word ):
        if( len( self.data ) < self.size_max ):
            self.data.append( word )
        else:
            self.data = self.data[1:]
            self.data.append( word )

###################################################################################################

class Client(threading.Thread):
    def __init__(self, id_ , name , target):
        super().__init__()
        self.id_ = id_
        self.name = name
        self.target = target
        self.target = ''

    def createSocket(self):
        print("bitch")
        self.sock = socket.socket( socket.AF_INET , socket.SOCK_STREAM )
        self.port = 7004
        self.sock.connect( ( self.target, self.port ) )
        self.sock.send( b"ppd" )

    def run(self):
        self.createSocket()

###################################################################################################

class Manager(threading.Thread):
    def __init__(self, id_ , name ):
        self.id_ = id_
        self.name = name

def main():
    serv =  Server( 2 , "roger" )
    client = Client( 2, "test" , '' )
    serv.start()
    client.start()



if __name__ == "__main__":
    main()
