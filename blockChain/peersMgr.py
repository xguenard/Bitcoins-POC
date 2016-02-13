import queue
import select
import threading
import consensus
import unittest

class PeersManager(threading.Thread):
    """
        This class is the interface with the network :
        - can get a list of peers wrote in a static file
        - have a list of active_peers
        - can create new connections with peers (from the file or by gui)
        - sending messages to all connected peers
        - listenning to all active peers
    """

    def __init__(self):
        super().__init__()
        self.peer_queue = queue.Queue()             #Peers newly connnected to the server
        self.message_queue = queue.Queue()          #Messages that I want to send to the others
        self.consensus = consensus.Consensus()      #Consensus, check all data and peers received
        self.active_peers = []                      #Active peer = active connection
        self.max_peers = 10
        self.number_peers = 0

    def ProcessPeerQ(self):
        """
            Adding peers received from the server side to the active peer list
        """
        while not self.peer_queue.empty() and self.number_peers <= self.max_peers:
            peer, addr = self.peer_queue.get()
            self.consensus.AddPeer( str(addr[0]) + "@" + str(addr[1]) )
            self.active_peers.append( peer )
            self.number_peers += 1
            self.peer_queue.task_done()

    def ProcessMessageQ(self, writable_peers ):
        """
            Processing the message queue, sending messages to all the peers
        """
        while not self.message_queue.empty():
            msg = self.message_queue.get()
            self.consensus.Add( msg )
            for peer in writable_peers:
                peer.send(msg.encode("utf-8") )
            self.message_queue.task_done()
    def Read(self, peer ):
        """
            Read the data received from an active peer
        """
        data = peer.recv(4096)
        if data:
            self.consensus.Add( data[:-2].decode("utf-8") )
        else:
            peer.close()


    def run(self):
        """
            Peer management using select
        """

        while True:
            print("Processing loop")
            self.ProcessPeerQ()

            readable, writable, execptions = select.select( self.active_peers \
                    , self.active_peers , [], 0.2 )

            #Read data
            for r in readable :
                self.Read( r )

            #Write data
            self.ProcessMessageQ( writable )

            #exceptions
            for e in execptions :
                print( e )

    #Getters methods for GUI and stuff
    def GetPeerQ(self):
        return self.peer_queue
    def GetMessQ(self):
        return self.message_queue
    def GetDataVis(self):
        return self.consensus.vis_data.model
    def GetMetaVis(self):
        return self.consensus.meta_data.model
    
    
class PeersManagerTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_threads(self):
        t = PeersManager()


if __name__ == "__main__":
    unittest.main()
