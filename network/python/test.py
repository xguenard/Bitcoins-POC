from PySide import QtCore, QtGui


model = QtGui.QStringListModel()
list = QtCore.QStringList()
list.append("a")
model.setStringList(list)
