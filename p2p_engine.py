import socket
import threading
from PySide import QtGui, QtCore
import sys

#Goal = create a simple p2p protocol.
#This will be used as a basis for ledging and broker apps

class ServerView(QtGui.QDialog):
    def __init__(self , model):
        super().__init__()
        self.model = model
        self.listView = QtGui.QListView()
        self.listView.setModel( self.model)
        layout = QtGui.QVBoxLayout()
        layout.addWidget( self.listView )
        self.setLayout( layout )
        self.show()

class ListModel(QtCore.QAbstractListModel):
    def __init__(self):
        super().__init__()
        self.data_list = ["one", "two"]

    def rowCount(self , index = QtCore.QModelIndex()):
        return len( self.data_list )

    def data( self, index, role ):
        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            value = self.data_list[ row ]
            return value

    def addElem( self, msg ):
        self.data_list.append( msg )
        index = self.createIndex( len( self.data_list) -1 , 0  )
        self.emit(QtCore.SIGNAL("dataChanged(QModelIndex, QModelIndex )"), index , index )

class ConsensusContainer():
    def __init__(self):
        self.model = ListModel()

    def addElem(self, msg ):
        self.model.addElem( msg )

################################################################################################

class ServerManager(threading.Thread):
    def __init__(self, id_ , name):
        super().__init__()
        self.id_ = id_
        self.name = name
        self.consensus = ConsensusContainer()
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
            self.connections_list.append( SConnection( addr , connection, self.consensus ))
            self.StartLastConnection()
        self.sock.close()

    def StartLastConnection(self):
        self.connections_list[-1].setDaemon(True)
        self.connections_list[-1].start()

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
##################################################################################################
class ClientContainer():
    def __init__(self):
        self.model = ListModel()

    def addElem(self, msg ):
        self.model.addElem( msg )


class ClientView(QtGui.QDialog):
    def __init__(self, model, cli_manager ):
        super().__init__()
        self.model = model
        self.cli_manager = cli_manager
        self.listview = QtGui.QListView()
        self.listview.setModel( self.model)
        self.lineedit = QtGui.QLineEdit("entrer message ici :" )
        self.lineedit.selectAll()
        layout = QtGui.QVBoxLayout()
        layout.addWidget( self.listview )
        layout.addWidget( self.lineedit )

        self.connect( self.lineedit, QtCore.SIGNAL("returnPressed()"), self.updateui )
        self.setLayout( layout )
        self.show()

    def updatedata( self ):
        msg = self.lineedit.text()
        self.lineedit.setText("")
        self.cli_manager.sendAll( msg )

    def updateui( self ):
        self.updatedata()

###################################################################################################

class ClientsManager():
    def __init__(self, target_list):
        super().__init__()
        self.container = ClientContainer()
        self.target_list = target_list
        self.clients_list = []
        self.thread_list = []
        self.initAll()

    def GetModel(self):
        return self.container.model

    def initAll( self ):
        i = 0 
        for targ in self.target_list:
            self.clients_list.append( Client( i , "TEST" , targ[0] ))
            i += 1
            
    def sendAll(self, msg ):
        self.container.addElem( msg )
        self.thread_list = []

        for cli in self.clients_list:
            self.thread_list.append( threading.Thread( target = cli.SendMsg , args = (msg, )))

        for thr in self.thread_list:
            thr.start()
        for thr in self.thread_list:
            thr.join()



class Client():
    def __init__(self, id_ , name , target):
        self.id_ = id_
        self.name = name
        self.target = target
        self.createSocket()

    def createSocket(self):
        self.sock = socket.socket( socket.AF_INET , socket.SOCK_STREAM )
        self.port = 7004
        self.sock.connect( ( self.target, self.port ) )
        self.sock.send( self.name.encode("utf-8"))

    def SendMsg(self, msg ):
        self.sock.send( msg.encode("utf-8"))


###################################################################################################

class Manager(threading.Thread):
    def __init__(self, id_ , name ):
        self.id_ = id_
        self.name = name

def main():
    app = QtGui.QApplication(sys.argv)
    serv =  ServerManager( 2 , "roger" )
    serv_view = ServerView( serv.GetModel() )
    targ_list = [ ["", 7004] ]
    serv.start()
    clis = ClientsManager( targ_list )
    cli_view = ClientView( clis.GetModel() , clis )
    app.exec_()


if __name__ == "__main__":
    main()
