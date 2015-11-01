import threading
import dataMgr
import socket
import connectionMgr


class ServerManager(threading.Thread):
    def __init__(self, id_ , name):
        super().__init__()
        self.id_ = id_
        self.name = name
        self.consensus = dataMgr.ConsensusContainer()
        self.CreateSockets()
        self.connections_list = []

    def GetModel(self):
        return self.consensus.model

    def CreateSockets(self):
        self.sock = socket.socket( socket.AF_INET , socket.SOCK_STREAM )
        self.host = ''
        self.port = 7004 
        self.sock.bind( (self.host , self.port) )
        self.sock.listen(10)

    def run(self):
        self.Listening()

    def Listening(self):
        while True:
            print("waiting for connections")
            connection , addr  = self.sock.accept()
            print(" connected with : " + addr[ 0] + " : " + str( addr[1] ) )
            self.connections_list.append( connectionMgr.SConnection( addr , connection, self.consensus ))
            self.StartLastConnection()
        self.sock.close()

    def StartLastConnection(self):
        self.connections_list[-1].setDaemon(True)
        self.connections_list[-1].start()


