from PySide import QtCore, QtGui
import sys



class ConnectionWidget( QtGui.QListView ):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI( self ):
        self.model = QtGui.QStringListModel()
        self.data = []
        self.data.append("test1")
        self.data.append("test2")
        self.model.setStringList( self.data )
        self.setModel( self.model )
        self.setGeometry( 400 , 400 , 400 , 400 )
        self.setWindowTitle("CONNECTION")
        self.show()

def main():

    app = QtGui.QApplication(sys.argv)
    ex = ConnectionWidget()
    sys.exit( app.exec_() )

if __name__ == "__main__":
    main()
