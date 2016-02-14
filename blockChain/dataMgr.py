import dataModels





def CreateContainers():
    return MetaContainer() , NetworkContainer()
   

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
        Should print data about the application, if a peers is correctly added to the
        network for example
    """
    def __init__(self):
        self.model = dataModels.ListModel()

    def add(self, msg ):
        self.model.addElem( msg )


class NetworkContainer():

    def __init__(self):
        self.model = dataModels.ListModel()


