import socket
import threading
from PySide import QtGui, QtCore
import sys
import dataModels
import mainGui
import clientMgr
import serverMgr
import dataMgr

#Goal = create a simple p2p protocol.
#This will be used as a basis for ledging and broker apps

def main():
    app = QtGui.QApplication(sys.argv)
    serv =  serverMgr.ServerManager( 2 , "roger" )
    serv_view = mainGui.ServerView( serv.GetModel() )
    targ_list = [ ["",7004 ] ]
    serv.start()
    clis = clientMgr.ClientsManager( targ_list )
    cli_view = mainGui.ClientView( clis.GetModel() , clis )
    wind =  mainGui.MainWindow( serv_view , cli_view) 
    app.exec_()


if __name__ == "__main__":
    main()
