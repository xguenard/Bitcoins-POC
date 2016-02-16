from PySide import QtGui, QtCore



def initialize_gui(cons_model, meta_model, msg_q , peer_creator):
    msg_view = MessageView(msg_q)
    peer_view = PeerView(peer_creator)
    cons_view = ConsenusView(cons_model)
    meta_view = MetaDataView(meta_model)
    return MainWindow(msg_view, peer_view, cons_view, meta_view)



# left column = message view and peer view
class MessageView(QtGui.QDialog):
    def __init__(self, msg_q):
        super().__init__()
        self.msg_q = msg_q
        self.lineedit = QtGui.QLineEdit("Message :" )
        self.lineedit.selectAll()
        self.connect( self.lineedit, QtCore.SIGNAL("returnPressed()")\
                , self.updatedata)
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.lineedit)
        self.setLayout(layout)
    
    def updatedata(self):
        msg = self.lineedit.text()
        self.lineedit.setText("")
        self.msg_q.put( msg )

class PeerView(QtGui.QDialog):
    def __init__(self, peer_creator):
        super().__init__()
        self.peer_creator = peer_creator

        self.line_ip = QtGui.QLineEdit("Target IP")
        self.line_ip.selectAll()

        self.line_port = QtGui.QLineEdit("Target port")
        self.line_port.selectAll()

        self.ok_button = QtGui.QPushButton("Add peer")

        self.connect( self.ok_button , QtCore.SIGNAL("clicked()")\
                , self.updatedata)

        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.line_ip)
        layout.addWidget(self.line_port)
        layout.addWidget(self.ok_button)
        self.setLayout(layout)

    def updatedata(self):
        ip = self.line_ip.text()
        port = int(self.line_port.text())

        self.line_ip.setText("")
        self.line_port.setText("")

        self.peer_creator.create_peer( ip, port )

#Mid column = consensusView
class ConsenusView(QtGui.QDialog):
    def __init__(self , model):
        super().__init__()
        self.model = model
        self.listView = QtGui.QListView()
        self.listView.setModel( self.model)
        layout = QtGui.QVBoxLayout()
        layout.addWidget( self.listView )
        self.setLayout( layout )

#Right column = Metadata
class MetaDataView(QtGui.QDialog):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.listview = QtGui.QListView()
        self.listview.setModel( self.model)
        layout = QtGui.QVBoxLayout()
        layout.addWidget( self.listview )
        self.setLayout( layout )


# MainWindow to order all
class MainWindow(QtGui.QWidget):
    def __init__(self, msg_view, peer_view, cons_view , meta_view ):
        super().__init__()
        self.msg_view = msg_view
        self.peer_view = peer_view
        self.cons_view = cons_view
        self.meta_view = meta_view
        self.initUI()

    def initUI(self):
        self.setGeometry( 800,800, 800, 800 )
        v_layout = QtGui.QVBoxLayout()
        v_layout.addWidget(self.msg_view)
        v_layout.addWidget(self.peer_view)

        layout = QtGui.QHBoxLayout()
        layout.addLayout(v_layout)
        layout.addWidget(self.cons_view)
        layout.addWidget(self.meta_view)
        self.setLayout(layout)
        self.show()
