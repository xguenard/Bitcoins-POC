import queue
import dataMgr


class Infos:
    """
        class used to log information on the gui and in the log file
    """
    def __init__(self):
        self.vis_data = dataMgr.MetaContainer()
        self.peer_set = set()

    def AddPeer(self, name ):
        if not name in self.peer_set:
            if self.VerifyPeer( name ):
                self.peer_set.add( name )
                self.vis_data.addElem( name )

    def Add(self, message):
            self.vis_data.addElem( message )
