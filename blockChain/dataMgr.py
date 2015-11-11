import dataModels

class ConsensusContainer():
    def __init__(self):
        self.model = dataModels.ListModel()

    def addElem(self, msg ):
        self.model.addElem( msg )


class ClientContainer():
    def __init__(self):
        self.model = dataModels.ListModel()

    def addElem(self, msg ):
        self.model.addElem( msg )


