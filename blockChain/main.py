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
    port = int(input("Enter port :\n"))
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
    serv.start()
    
    peer_creator = serverMgr.PeerCreator(peer_mgr.get_peer_Q(), meta)

    #Init GUI
    wind = mainGui.initialize_gui(cons.vis_data.model, meta.model\
            , peer_mgr.get_mess_Q(), peer_creator)
    app.exec_()


if __name__ == "__main__":
    main()
