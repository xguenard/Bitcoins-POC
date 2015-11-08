import threading
import dataMgr
import client

class ClientsManager():
    def __init__(self, target_list):
        super().__init__()
        self.container = dataMgr.ClientContainer()
        self.target_list = target_list
        self.clients_list = []
        self.thread_list = []
        self.initAll()

    def GetModel(self):
        return self.container.model

    def initAll( self ):
        i = 0 
        for targ in self.target_list:
            self.clients_list.append( client.Client( i , "TEST" , targ[0] ))
            i += 1
            
    def sendAll(self, msg ):
        self.container.addElem( msg )
        self.thread_list = []

        for cli in self.clients_list:
            self.thread_list.append( threading.Thread( target = cli.SendMsg , args = (msg, )))

        for thr in self.thread_list:
            thr.start()
        for thr in self.thread_list:
            thr.join()
