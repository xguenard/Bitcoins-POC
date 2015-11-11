import queue
import dataMgr


class Consensus:
    """Future crypto structure for validation and algorithms test"""
    def __init__(self):
        self.vis_data = dataMgr.ConsensusContainer()


    def Add(self, message):
        """No verification for the moment"""
        self.vis_data.addElem( message )
