import socket
import threading

class SConnection(threading.Thread):
    def __init__(self, addr , connection ):
        super().__init__()
        self.addr = addr
        self.connection = connection
        self.size_max = 20

    def run(self):
        self.ReceiveData()

    def ReceiveData(self):
        while True:
            tmp_data = self.connection.recv(4096).decode("utf-8")
            if tmp_data:
                self.AddToData( tmp_data)
                self.connection.send( b"Message Receved" )

    def SendMsg(self, msg ):
        self.connection.send( msg.encode("utf-8"))

    def AddToData(self, word ):
        self.consensus.addElem( word )



class ConnectionManager():
    def __init__(self):
        self.conn_dict = {}
        self.addr_set = set()
        self.red_dico = []

    def Add(self, connection, addr ):
        """Red List Management to add"""
        if addr not in self.red_dico:
            self.conn_dict[ addr ] = SConnection( addr, connection )
            self.conn_dict[ addr ].start()
            self.addr_set.add( addr )
        else:
            print("Red Listed connection from : " + addr )

   def SendAll( self, message , sending_addr):
       """To do, improve by adding all the other nodes"""
       for addr, conn in self.conn_dict.iteritems():
           if addr != sending_addr :
               conn.SendMsg( message.encode("utf-8"))
