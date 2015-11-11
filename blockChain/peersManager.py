import Queue


class PeersManager(Threading.Thread):
    """Have to add locks"""
    def __init__(self, queue):
        super().__init__()
        self.peer_q = Queue.Queue()
        self.message_q = Queue.Queue()

        self.active_peers = []                      #Active peer = active connection
        self.message_q = ["Hello", "World"]
        self.max_peers = 10
        self.number_peers = 0

    def ProcessPeerQ(self):
        while !self.peer_queue.empty() and self.number_peers <= self.max_peers:
            peer = self.peer_queue.get()
            self.active_peers.append( peer )
            self.number_peers += 1
            self.queue.task_done()

    def ProcessMessageQ(self, writable_peers ):
        while !self.message_q.empty():
            msg = self.message_q.get()
            for peer in writable_peers:
                peer.send(msg) 
            self.message_q.task_done()

    def run(self):
        self.ProcessPeerQ()
