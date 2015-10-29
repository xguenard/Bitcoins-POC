from PySide import QtGui, QtCore
import sys



class testForm(QtGui.QDialog):

    def __init__(self):
        super().__init__()
        self.cont = InfoContainer()
        self.model = DataModel()
        self.browser = QtGui.QListWidget()
        self.lineedit = QtGui.QLineEdit("Entrer message ici")
        self.lineedit.selectAll()
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.lineedit)
        self.setLayout(layout)
        self.lineedit.setFocus()
        self.connect( self.lineedit, QtCore.SIGNAL("returnPressed()"),
                self.updateUi)
        self.setWindowTitle("testouille")
        self.show()


    def updateUi(self):
        msg = self.lineedit.text()
        self.lineedit.setText("")
        self.cont.add( msg )
        self.updateList()

    def updateList(self):
        self.browser.clear()
        for str_ in self.cont.data :
            self.browser.addItem( str_)



class DataModel(QtCore.QAbstractListModel):

    def __init__(self):
        super().__init__()
        self.cont = InfoContainer()


    def rowCount(self):
        return self.cont.size()

    def data(self, id_):
        return self.cont.data[ id_ ]

    def dataChanged( self, id_ ):
        self.emit( QtCore.SIGNAL("dataChanged(QModelIndex, QModelIndex)"), id_ , id_ )

class InfoContainer():
    def __init__(self):
        self.data = []

    def add(self, msg ):
        self.data.append( msg )

    def size(self):
        return len( self.data )

if __name__ == "__main__":
    print("Launching Gui")
    app = QtGui.QApplication(sys.argv)
    tt = testForm()
    app.exec_()
