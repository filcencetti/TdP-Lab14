import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._idMap = {}

    def getStores(self):
        return DAO.getStores()

    def buildGraph(self,store,K):
        self._graph = nx.DiGraph()
        allNodes = DAO.getNodes(int(store))
        self._graph.add_nodes_from(allNodes)
        for i in allNodes:
            self._idMap[i.order_id] = i

        allEdges = DAO.getEdges(store,K)
        for edge in allEdges:
            if edge.date1 < edge.date2:
                self._graph.add_edge(self._idMap[edge.id2],self._idMap[edge.id1],weight=edge.quantity)

            elif edge.date1 > edge.date2:
                self._graph.add_edge(self._idMap[edge.id1], self._idMap[edge.id2], weight=edge.quantity)
    def getPath(self,node):

        path = self._graph.successors(self._idMap[node])
        return path