from PySide import QtCore

class ListModel(QtCore.QAbstractListModel):
    """
        Model used to keep Gui updated with our data
    """

    def __init__(self):
        super().__init__()
        self.data_list = []

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
        self.emit(QtCore.SIGNAL("dataChanged(QModelIndex, QModelIndex )")\
                , index , index )
