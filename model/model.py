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
            self._graph.add_edge(self._idMap[edge[0]],self._idMap[edge[1]],weight=edge[2])

    def getPath(self,node):
        source = self._idMap[node]
        lp = []

        # for source in self._graph.nodes:
        tree = nx.dfs_tree(self._graph, source)
        nodes = list(tree.nodes())

        for node in nodes:
            tmp = [node]

            while tmp[0] != source:
                pred = nx.predecessor(tree, source, tmp[0])
                tmp.insert(0, pred[0])

            if len(tmp) > len(lp):
                lp = copy.deepcopy(tmp)

        return lp

    def getMaxWeightedPath(self, node_start):
        self._bestPath = []
        self._bestScore = 0

        parziale = [self._idMap[node_start]]

        for v in self._graph.neighbors(self._idMap[node_start]): # == self._graph.successors()
            parziale.append(v)
            self.recursion(parziale)
            parziale.pop()

        return self._bestPath, self._bestScore

    def recursion(self, parziale):
        if self.getScore(parziale) > self._bestScore:
            self._bestScore = self.getScore(parziale)
            self._bestPath = copy.deepcopy(parziale)

        for v in self._graph.neighbors(parziale[-1]): # == self._graph.successors()
            if (v not in parziale and  # check if not in parziale
            self._graph[parziale[-2]][parziale[-1]]["weight"] > self._graph[parziale[-1]][v]["weight"]):  # check if peso nuovo arco è minore del precedente
                parziale.append(v)
                self.recursion(parziale)
                parziale.pop()

    def getScore(self, path):
        tot = 0
        for i in range(len(path) - 1):
            tot += self._graph[path[i]][path[i + 1]]["weight"]

        return tot