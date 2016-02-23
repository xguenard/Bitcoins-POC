import queue
import select
import threading
import consensus
import unittest
import time

class PeersManager(threading.Thread):
    """
        This class is the interface with the network :
        - can get a list of peers wrote in a static file
        - have a list of active_peers
        - can create new connections with peers (from the file or by gui)
        - sending messages to all connected peers
        - listenning to all active peers
    """

    def __init__(self, cons , meta):
        super().__init__()
        #Peers newly connnected to the server
        self.peer_queue = queue.Queue()  
        #Messages that I want to send to the others
        self.message_queue = queue.Queue()
        #Consensus, check all data and peers received
        self.consensus = cons
        self.metas_infos = meta
        #Active peer = active connection
        self.active_peers = []
        self.max_peers = 10
        self.number_peers = 0

    def process_peer_Q(self):
        """
            Adding peers received from the server 
            side to the active peer list
        """
        while not self.peer_queue.empty() \
                and len(self.active_peers) <= self.max_peers:

            peer, addr = self.peer_queue.get()
            self.consensus.add_peer(str(addr[0]) + "@" + str(addr[1]))
            self.active_peers.append( peer )
            self.peer_queue.task_done()

    def process_message_Q(self, writable_peers ):
        """
            Processing the message queue, sending messages to all the peers
        """
        while not self.message_queue.empty():
            msg = self.message_queue.get()
            self.consensus.add(msg)
            self.metas_infos.add( \
                    "Sending a message '{}' to {} connected peers".format(\
                    msg, len(self.active_peers)))
  
            for peer in writable_peers:
                r=peer.send(msg.encode("utf-8"))
            self.message_queue.task_done()

    def read(self, peer ):
        """
            Read the data received from an active peer.
            It may be a closing message.
        """
        data = peer.recv(4096)
        if data:
            self.consensus.add( data.decode("utf-8") )
            return True
        else:
            peer.close()
            return False

    def run(self):
        """
            Peer management using select
        """
        while True:
            #print("Processing loop")
            time.sleep(0.1)
            self.process_peer_Q()
            if( self.active_peers ):
                readable, writable, execptions = select.select(\
                        self.active_peers, self.active_peers, [], 0.2)
                #Read data
                for r in readable :
                    if not self.read(r):
                        self.active_peers.remove(r)

                self.process_message_Q(writable)
            else:
                time.sleep(0.2)
            #Write data

    #Getters methods for GUI and stuff
    def get_peer_Q(self):
        return self.peer_queue

    def get_mess_Q(self):
        return self.message_queue

    def get_data_vis(self):
        return self.consensus.vis_data.model

    def get_meta_vis(self):
        return self.metas_infos.meta_data.model

#Tests for the GUI only
class TestPeer(threading.Thread):
    def __init__(self, cons, meta):
        super().__init__()
        self.message_queue = queue.Queue()
        self.consensus = cons
        self.metas_infos = meta

    def process_message_Q(self):
        """
            Processing the message queue, sending messages to all the peers
        """
        while not self.message_queue.empty():
            msg = self.message_queue.get()
            self.consensus.add(msg)
            self.metas_infos.add( \
                    "Sending a message '{}' to {} connected peers".format(\
                    msg, 0))

    def run(self):
        while True:
            time.sleep(0.1)
            self.process_message_Q()

    def get_mess_Q(self):
        return self.message_queue
