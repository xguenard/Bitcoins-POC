from PySide import QtCore, QtGui
import sys
import threading


class ConnectionWidget( QtGui.QListView ):

    def __init__(self , data):
        super().__init__()
        self.data = data
        self.initUI()

    def initUI( self ):
        self.model = QtGui.QStringListModel(self.data)
        self.setModel( self.model )

class MainWidget(QtGui.QWidget):
    def __init__(self, datas ):
        super().__init__()
        self.datas = datas
        self.initUI()

    def initUI( self ):
        grid = QtGui.QGridLayout()
        self.widgClient = ConnectionWidget( self.datas[0] ) 
        self.widgServer = ConnectionWidget( self.datas[1] ) 
        grid.addWidget( self.widgClient ) 
        grid.addWidget( self.widgServer )
        self.setLayout( grid )
        self.setWindowTitle("TEST")
        self.show()


class GUIManager(threading.Thread):
    def __init__(self):
        super().__init__()
        self.list1 = [ "xavier" , "tetris"]
        self.list2 = [ "rouquin", "test" ]
        self.widg = MainWidget( [ self.list1, self.list2 ] )

    def run( self ):
        print("Running")
        self.widg.widgClient.data.append("trois")
        self.widg.widgClient.dataChanged( 1 , 1 )
        self.widg.update()
        self.widg.widgClient.update()
        print("Running1")

def main():
    app = QtGui.QApplication(sys.argv)
    a = GUIManager()
    a.start()
    app.exec_()
    sys.exit()

if __name__ == "__main__":
    main()
