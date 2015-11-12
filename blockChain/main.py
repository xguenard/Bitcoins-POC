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

    #Init consensu View
    cons_view = mainGui.ConsenusView( peer_mgr.GetDataVis() )

    #Init Client view
    meta_view = mainGui.MetaDataView( peer_mgr.GetMessQ() , peer_mgr.GetMetaVis() )

    #Init and Launch Main View
    wind =  mainGui.MainWindow( cons_view , meta_view ) 
    app.exec_()


if __name__ == "__main__":
    main()
