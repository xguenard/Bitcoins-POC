import dataModels

class ConsensusContainer():
    """
        Contains data of the consensus informations
        - should be use to verify that 2 peers have the same consensus
    """
    def __init__(self):
        self.model = dataModels.ListModel()

    def addElem(self, msg ):
        self.model.addElem( msg )


class MetaContainer():
    """
        Should print data about the peers connected on the network
        - Actually used to print what I am wrinting
    """
    def __init__(self):
        self.model = dataModels.ListModel()

    def addElem(self, msg ):
        self.model.addElem( msg )


