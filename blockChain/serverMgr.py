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
        self.sock.listen(5)

    def run(self):
        self.Listening()

    def Listening(self):
        while True:
            print("waiting for connections")
            connection , addr  = self.sock.accept()
            print(" connected with : " + addr[ 0] + " : " + str( addr[1] ) )

            self.connections_list.append( connectionMgr.SConnection( 
                addr , connection, self.consensus ))

            self.StartLastConnection()

        self.sock.close()

    def StartLastConnection(self):
        self.connections_list[-1].setDaemon(True)
        self.connections_list[-1].start()



class PeersManager:
    def __init__(self):
        self.active_peers = {}
        self.unactive_peers = set()
        self.peers_list = set()
        self.max_peers = 10

    def AddPeer(self, conn = None , addr = '' , port = '' ):
        if conn != None:
            self.active_peers[ ( addr, port ) ] = conn
        else:
            self.peers_list.add( (addr, port ) ]


    def sendAll( self , msg ):
        for key, conn in self.active_peers.items:
            try:
                conn.sendall( msg.encode("utf-8"))
            except:
                del self.active_peers[ key ]
                self.unactive_peers.add( key )

class Peer(Threading.Thread):
    def __init__(self, addr, port, conn):
        super().__init__()
        self.addr = addr
        self.port = port
        self.conn = conn


            



class Consensus:
    def Validate(self, arg):
        pass

