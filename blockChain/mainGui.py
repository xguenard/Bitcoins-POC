from PySide import QtGui, QtCore



class ServerView(QtGui.QDialog):
    def __init__(self , model):
        super().__init__()
        self.model = model
        self.listView = QtGui.QListView()
        self.listView.setModel( self.model)
        layout = QtGui.QVBoxLayout()
        layout.addWidget( self.listView )
        self.setLayout( layout )

class ClientView(QtGui.QDialog):
    def __init__(self,  msg_q , model):
        super().__init__()
        self.model = model
        self.msg_q = msg_q
        self.listview = QtGui.QListView()
        self.listview.setModel( self.model)
        self.lineedit = QtGui.QLineEdit("entrer message ici :" )
        self.lineedit.selectAll()
        layout = QtGui.QVBoxLayout()
        layout.addWidget( self.listview )
        layout.addWidget( self.lineedit )

        self.connect( self.lineedit, QtCore.SIGNAL("returnPressed()"), self.updateui )
        self.setLayout( layout )

    def updatedata( self ):
        msg = self.lineedit.text()
        self.lineedit.setText("")
        self.msg_q.put( msg )

    def updateui( self ):
        self.updatedata()

class MainWindow(QtGui.QWidget):
    def __init__(self, serv_view , cli_view ):
        super().__init__()
        print("ici")
        self.serv_view = serv_view
        self.cli_view = cli_view
        self.initUI()

    def initUI(self):
        self.setGeometry( 400,400, 400, 400 )
        layout = QtGui.QHBoxLayout()
        layout.addWidget( self.cli_view )
        layout.addWidget( self.serv_view )
        self.setLayout( layout )
        self.show()
