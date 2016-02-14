import queue
import dataMgr


class Consensus:
    """
        Future crypto structure for validation and algorithms test
    """
    def __init__(self):
        self.vis_data = dataMgr.ConsensusContainer()
        self.peer_set = set()

    def add_peer(self, name ):
        if not name in self.peer_set:
            if self.verify_peer( name ):
                self.peer_set.add( name )

    def add(self, message):
        """
            No verification for the moment
        """
        if self.verify_message( message ):
            self.vis_data.addElem( message )

    def verify_message( self, message ):
        return True

    def verify_peer( self, name ):
        return True
