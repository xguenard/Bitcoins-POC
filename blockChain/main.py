import socket
import threading
from PySide import QtGui, QtCore
import sys
import dataModels
import mainGui
import serverMgr
import peersMgr
import dataMgr
import consensus

#Goal = create a simple p2p protocol.
#This will be used as a basis for ledging and broker apps

def main():
    #For test only, ask for the port

    port =int(input("Enter port number\n"))
    port2 =int(input("port to connect\n"))
    #Init Graphical env
    app = QtGui.QApplication(sys.argv)
    
    #Init data containers for GUI
    meta , net = dataMgr.CreateContainers()
    cons = consensus.Consensus()

    #Init Peer Manager
    peer_mgr = peersMgr.PeersManager( cons, meta)
    peer_mgr.start()

    #Init server 
    serv =  serverMgr.ServerManager(peer_mgr.get_peer_Q(), meta, port)
    serv.new_peers_queue.put( ('' , port2))
    serv.start()

    #Init consensu View
    cons_view = mainGui.ConsenusView( cons.vis_data.model )

    #Init Client view
    meta_view = mainGui.MetaDataView( peer_mgr.get_mess_Q() , meta.model )

    #Init and Launch Main View
    wind =  mainGui.MainWindow( cons_view , meta_view ) 
    app.exec_()


if __name__ == "__main__":
    main()
