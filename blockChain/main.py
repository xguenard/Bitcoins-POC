import socket
import threading
from PySide import QtGui, QtCore
import sys
import dataModels
import mainGui
import serverMgr
import peersMgr

#Goal = create a simple p2p protocol.
#This will be used as a basis for ledging and broker apps

def main():
    #Init Graphical env
    app = QtGui.QApplication(sys.argv)

    #Init Peer Manager
    peer_mgr = peersMgr.PeersManager()
    peer_mgr.start()

    #Init server 
    serv =  serverMgr.ServerManager( peer_mgr.GetPeerQ() )
    serv.start()

    #Init server View
    serv_view = mainGui.ServerView( peer_mgr.GetDataVis() )

    #Init Client view
    cli_view = mainGui.ClientView( peer_mgr.GetMessQ() , dataModels.ListModel() )

    #Init and Launch Main View
    wind =  mainGui.MainWindow( serv_view , cli_view ) 
    app.exec_()


if __name__ == "__main__":
    main()
