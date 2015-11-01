import socket
import threading

class SConnection(threading.Thread):
    def __init__(self, addr , connection , consensus):
        super().__init__()
        self.addr = addr
        self.connection = connection
        self.consensus = consensus
        self.size_max = 20

    def run(self):
        self.ReceiveData()

    def ReceiveData(self):
        while True:
            tmp_data = self.connection.recv(4096).decode("utf-8")
            if tmp_data:
                self.AddToData( tmp_data)
                self.connection.send( b"Message Receved" )

    def AddToData(self, word ):
        self.consensus.addElem( word )
