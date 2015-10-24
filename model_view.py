from PySide import QtGui, QtCore
import sys
import time
import threading





class dataModel(QtCore.QAbstractListModel):
    def __init__(self):
        super().__init__()
        self.data_list = ["one", "two"]
        t = threading.Thread( target = self.addMsg)
        t.setDaemon(True)
        t.start()

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

    def addMsg( self ):
        while True:
            time.sleep( 2 )
            self.addElem("YES")

class MainView(QtGui.QDialog):
    def __init__(self):
        super().__init__()
        self.model = dataModel()
        self.listView = QtGui.QListView()
        self.listView.setModel( self.model)
        self.lineedit = QtGui.QLineEdit("Entrer message ici :" )
        self.lineedit.selectAll()
        layout = QtGui.QVBoxLayout()
        layout.addWidget( self.listView )
        layout.addWidget( self.lineedit )

        self.connect( self.lineedit, QtCore.SIGNAL("returnPressed()"), self.updateUi )
        self.setLayout( layout )
        self.show()

    def updateData( self ):
        msg = self.lineedit.text()
        self.lineedit.setText("")
        self.model.addElem( msg )

    def updateUi( self ):
        self.updateData()



##
app = QtGui.QApplication(sys.argv)
m = MainView()
app.exec_()



