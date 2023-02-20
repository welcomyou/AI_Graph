class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
        self.color = 'white'
        self.distance = 0
        self.pred = None
        # for dfs
        self.discovery = 0
        self.finish = 0

    def addNeighbor(self,nbr,weight=0): #key chính là object
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

    def getColor(self):
        return self.color
    def setColor(self, color):
       self.color = color

    def getDistance(self):
        return self.distance
    def setDistance(self, distance):
        self.distance = distance

    def getPred(self):
        return self.pred
    def setPred(self, previous_node):
        self.pred = previous_node

    def getDiscovery (self):
        return self.discovery
    def setDiscovery (self, discovery_time):
        self.discovery = discovery_time

    def getFinish (self):
        return self.finish
    def setFinish (self, finish_time):
        self.finish = finish_time