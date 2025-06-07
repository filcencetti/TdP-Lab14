from model.model import Model

mymodel = Model()
mymodel.buildGraph(2,5)
print(mymodel._graph.number_of_nodes())
for i in mymodel.getPath(10):
    print(i)
print(mymodel.getMaxWeightedPath(10))