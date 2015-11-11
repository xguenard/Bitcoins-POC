import queue
import select
import threading
import consensus
import unittest

class PeersManager(threading.Thread):
    def __init__(self):
        super().__init__()
        self.peer_queue = queue.Queue()
        self.message_queue = queue.Queue()
        self.consensus = consensus.Consensus()
        self.active_peers = []                      #Active peer = active connection
        self.max_peers = 10
        self.number_peers = 0

    def ProcessPeerQ(self):
        """Adding peers to the active peers list"""
        while not self.peer_queue.empty() and self.number_peers <= self.max_peers:
            peer = self.peer_queue.get()
            self.active_peers.append( peer )
            self.number_peers += 1
            self.peer_queue.task_done()

    def ProcessMessageQ(self, writable_peers ):
        """Processing the message queue"""
        while not self.message_queue.empty():
            msg = self.message_queue.get()
            print(msg)
            self.consensus.Add( msg )
            for peer in writable_peers:
                peer.send(msg.encode("utf-8") )
            self.message_queue.task_done()

    def GetPeerQ(self):
        return self.peer_queue

    def GetMessQ(self):
        return self.message_queue

    def GetDataVis(self):
        return self.consensus.vis_data.model

    def Read(self, peer ):
        data = peer.recv(4096)
        if data:
            data = data.decode("utf-8")
            self.consensus.Add( data )
            print( data )
        else:
            peer.close()

    def run(self):
        """Peer management using select"""

        while True:
            self.ProcessPeerQ()

            readable, writable, execptions = select.select( self.active_peers 
                    , self.active_peers , [], 1 )

            #Read data
            for r in readable :
                self.Read( r )

            #Write data
            self.ProcessMessageQ( writable )

            #exceptions
            for e in execptions :
                print( e )



class PeersManagerTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_threads(self):
        t = PeersManager()


if __name__ == "__main__":
    unittest.main()
