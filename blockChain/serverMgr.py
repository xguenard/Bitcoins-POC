import threading
import socket
import peersMgr
import queue


class ServerManager(threading.Thread):
    """
        Server side class, listen to new connection
    """
    def __init__(self, peer_queue , meta, port): 
        super().__init__()
        self.peer_queue = peer_queue
        self.port = port
        self.create_sockets()
        self.stop_listen = False 
        self.metas_info = meta

    def create_sockets(self):
        self.sock = socket.socket( socket.AF_INET , socket.SOCK_STREAM )
        self.sock.setsockopt( socket.SOL_SOCKET , socket.SO_REUSEADDR , 1 )
        self.host = ''
        self.sock.bind( (self.host , self.port) )
        self.sock.listen(5)

    def run(self):
        self.listening()

    def listening(self):
        while True and not self.stop_listen:
            print("waiting for connections")
            connection , addr  = self.sock.accept()
            print(" connected with : " + addr[0] + " : " + str(addr[1]))
            self.metas_info.add("New connection requeste from {} @ {}.".format(\
                    addr[0], str(addr[1])))
            connection.setblocking(0)
            self.peer_queue.put((connection, addr))

        self.sock.close()

class PeerCreator:
    def __init__(self, peer_queue, meta):
        self.peer_queue = peer_queue
        self.metas_info = meta

    def create_peer(self, tcp_ip, port):
        try:
            new_sock = socket.socket( socket.AF_INET , socket.SOCK_STREAM )
            new_sock.settimeout(10)
            new_sock.connect((tcp_ip, port))
            new_sock.setblocking(0)
        except socket.error as e:
            self.metas_info.add(\
                    "failed trying to connect to {} at {}.".format(\
                    tcp_ip, port))
            return
        self.peer_queue.put((new_sock, (tcp_ip, port)))
        self.metas_info.add(( "Connected to {} at {}.".format(\
                tcp_ip, port)))


class TestPeerCreator:
    def __init__(self, msg_queue, meta):
        self.msg_queue = msg_queue
        self.metas_info = meta

    def create_peer(self, tcp_ip, port):
        self.metas_info.add( "No peer creation in GUI TEST MODE")
