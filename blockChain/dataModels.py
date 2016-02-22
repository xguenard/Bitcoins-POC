from PySide import QtCore

#Elements of the list for the GUI
class ListItem(QtCore.QObject):
    def __init__(self, msg):
        super().__init__()
        self._msg = msg
    
    def _text(self):
        return self._msg

    changed = QtCore.Signal()
    msg = QtCore.Property(str, _text, notify=changed)

#List for the GUI
class ListModel(QtCore.QAbstractListModel):
    """
        Model used to keep Gui updated with our data
    """
    COLUMNS = ('MSG',)
    def __init__(self):
        super().__init__()
        self.data_list = [] #List of ListItems
        self.setRoleNames(dict(enumerate(ListModel.COLUMNS)))

    def rowCount(self , index = QtCore.QModelIndex()):
        return len( self.data_list )

    def data( self, index, role ):
        if index.isValid() and (role == self.COLUMNS.index('MSG') \
                or role == QtCore.Qt.DisplayRole ):
            return self.data_list[index.row()]._msg

    def addElem( self, msg ):
        self.beginInsertRows(QtCore.QModelIndex(), len(self.data_list)\
                , len(self.data_list))
        self.data_list.append( ListItem(msg))
        self.endInsertRows()
