from model.model import Model

mymodel = Model()
mymodel.buildGraph(1,5)
print(mymodel._graph.number_of_edges())
print(list(mymodel._graph.edges(mymodel._idMap[9],data=True)))
for i in mymodel.getPath(9):
    print(i)
mymodel.getMaxWeightedPath(9)
print(mymodel._bestScore)