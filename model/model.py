import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._idMap = {}
        self._longest_path = []

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
            self._graph.add_edge(self._idMap[edge.id1],self._idMap[edge.id2],weight=edge.quantity)

    def getPath(self,node):
        tree = nx.bfs_tree(self._graph, self._idMap[int(node)])
        nodi = list(tree.nodes())
        return nodi[1:]

    def getMaxWeightedPath(self,node):
        path = [self._idMap[node]]
        self._best_total = 0
        self._best_path = []
        total = 0
        max_weight = 10000
        self.recursion(path,total,max_weight)
        return self._best_path

    def recursion(self,path,total,max_weight):
        if total > self._best_total:
            self._best_total = total
            self._best_path = copy.deepcopy(path)

        for node in self._graph.successors(path[-1]):
            if node not in path:
                weight_edge = self._graph[path[-1]][node]["weight"]
                if weight_edge < max_weight:
                    total += weight_edge
                    path.append(node)
                    self.recursion(path, total, weight_edge)
                    total -= weight_edge
                    path.pop()