import queue
import dataMgr


class Consensus:
    """
        Future crypto structure for validation and algorithms test
    """
    def __init__(self):
        self.vis_data = dataMgr.ConsensusContainer()
        self.meta_data = dataMgr.MetaContainer()
        self.peer_set = set()

    def AddPeer(self, name ):
        if not name in self.peer_set:
            if self.VerifyPeer( name ):
                self.peer_set.add( name )
                self.meta_data.addElem( name )

    def Add(self, message):
        """
            No verification for the moment
        """
        if self.VerifyMessage( message ):
            self.vis_data.addElem( message )

    def VerifyMessage( self, message ):
        return True

    def VerifyPeer( self, name ):
        return True
