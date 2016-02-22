from PySide import QtCore, QtGui, QtDeclarative
import sys
import threading
import time

class commuicator(QtCore.QObject):
    sig = QtCore.Signal()

def do_it(sig):
    for i in range(0, 100):
        time.sleep(1)
        sig.emit()

app = QtGui.QApplication(sys.argv)

timer = QtCore.QTimer()
timer.start(2000)

my_obj = commuicator()

tmp = threading.Thread(target=do_it, args =(my_obj.sig,)) 

view = QtDeclarative.QDeclarativeView()
view.setSource(QtCore.QUrl('view.qml'))
root = view.rootObject()

my_obj.sig.connect(root.updateRotater)
tmp.start()

view.show()

sys.exit(app.exec_())
