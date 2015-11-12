import threading
import socket
import peersMgr
import queue


class ServerManager(threading.Thread):
    def __init__(self, peer_queue):
        super().__init__()
        self.peer_queue = peer_queue
        self.CreateSockets()

    def CreateSockets(self):
        self.sock = socket.socket( socket.AF_INET , socket.SOCK_STREAM )
        self.sock.setsockopt( socket.SOL_SOCKET , socket.SO_REUSEADDR , 1 )
        self.host = ''
        self.port = 7004 
        self.sock.bind( (self.host , self.port) )
        self.sock.listen(5)

    def run(self):
        self.Listening()

    def Listening(self):
        while True:
            print("waiting for connections")
            connection , addr  = self.sock.accept()
            print(" connected with : " + addr[ 0] + " : " + str( addr[1] ) )
            connection.setblocking(0)
            self.peer_queue.put( ( connection , addr )  )

        self.sock.close()
