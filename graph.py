import networkx as nx
import time as sleep
import tempfile
import os
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import pygraphviz as pgv
from typing import Text
from queue import Queue
from vertex import Vertex


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
        self.is_direct = False
        #dfs
        self.time = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
    def getVertices(self):
        return self.vertList.keys()

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,weight=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)


    def __iter__(self):
        return iter(self.vertList.values())

    def loadFromTextFile(self, fname: Text):
        """
        Read from text file (input folder)
        <Vertex ID> <list of linked Vertex>
        """
        with open(fname, "r") as f:
            #Get full Nodes list first
            for line in f:
                lstxt = line.strip().split(',')
                #Get Node
                self.addVertex(lstxt[0])
            #Time to get edges
            f.seek(0,0)
            for line in f:
                lstxt = line.strip().split(',')
                for i in range(1, len(lstxt)):
                    self.addEdge(lstxt[0], lstxt[i])

    def convertToNetworkX (self):
        """
        Don't use this function. Ugly drawing, not handle edge crossing well
        """
        # Create a graph
        nx_graph = nx.Graph()
        # Add vertices
        nx_graph.add_nodes_from([i for i in self.vertList.keys()])
        # Add edges with weights
        for f in self.vertList.keys(): #f là key ~ text
            for t in self.vertList[f].getConnections(): #t là 1 object
                nx_graph.add_edge(f, t.id, weight=self.vertList[f].getWeight(t))
        return nx_graph

    def convertToPyGraphviz (self):
        """
        Use this. Look nice!
        """
        # Create a graph
        pgv_graph = pgv.AGraph(directed=True if self.is_direct==True else False)
        # Add vertices
        for i in self.vertList.keys():
            pgv_graph.add_node(i)
            pgv_graph.get_node(i).attr['style']='filled'
        # Add edges with weights
        for f in self.vertList.keys(): #f là key ~ text
            for t in self.vertList[f].getConnections(): #t là 1 object
                pgv_graph.add_edge(f, t.id, weight=self.vertList[f].getWeight(t))
        return pgv_graph


    def drawNetworkX (self):
        """
        Don't use this function. Ugly drawing, not handle edge crossing well
        """
        nx_graph = self.convertToNetworkX()
        # Define a color map for the nodes
        color_map = [self.vertList[x].color for x in self.vertList]
        # Define the node to be colored
        #colored_node = 'A'
        # Draw the graph with labels, weights, and color
        pos = nx.spring_layout(nx_graph)
        nx.draw_networkx_nodes(nx_graph, pos, node_size=500, node_color=color_map, alpha=0.5)
        nx.draw_networkx_labels(nx_graph, pos)
        nx.draw_networkx_edges(nx_graph, pos)
        labels = nx.get_edge_attributes(nx_graph, 'weight')
        nx.draw_networkx_edge_labels(nx_graph, pos, edge_labels=labels)
        # Show the graph
        plt.show()
        return

    def drawPyGraphviz(self):
        """
        Use this. Look nice!
        """
        ag = self.convertToPyGraphviz()
        #ag = nx.nx_agraph.to_agraph(nx_graph)
        for i in self.vertList.keys():
            ag.get_node(i).attr['fillcolor'] = self.vertList[i].getColor()
        ag.layout(prog="dot")
        # A tip for not make an I/O file, but instead plotting on Plots view
        temp = tempfile.NamedTemporaryFile(delete=False)
        tempname = temp.name + ".png"
        ag.draw(tempname)
        img = mpimg.imread(tempname)
        plt.imshow(img)
        plt.show()
        os.remove(tempname)
        return

    def resetColornPred(self):
       self.time = 0
       for i in self.vertList.keys():
           self.vertList[i].setColor('white')
           self.vertList[i].setPred(None)


    def traverse(self, y):
        x = y
        while (x.getPred()):
            print(x.getId())
            x = x.getPred()
        print(x.getId())



    def bfs(self, startVertex, sleeptime=0):
        vertQueue = Queue()
        vertQueue.put(startVertex)
        while (vertQueue.qsize() > 0):
            currentVert = vertQueue.get()
            for nbr in currentVert.getConnections():
                if (nbr.getColor() == 'white'):
                    nbr.setColor('gray')
                    nbr.setDistance(currentVert.getDistance() + 1)
                    nbr.setPred(currentVert)
                    vertQueue.put(nbr)
            currentVert.setColor('yellow')
            self.drawPyGraphviz()
            sleep.sleep(sleeptime)


    def dfs(self,startVertex,sleeptime=0):
        startVertex.setColor('gray')
        self.drawPyGraphviz()
        sleep.sleep(sleeptime)
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.dfs(nextVertex)
        startVertex.setColor('yellow')
        self.drawPyGraphviz()
        self.time += 1
        startVertex.setFinish(self.time)


if __name__ == '__main__':
    print ("Go to main, plezz")