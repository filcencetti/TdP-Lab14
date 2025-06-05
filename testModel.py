from model.model import Model

mymodel = Model()
mymodel.buildGraph(1,5)
print(mymodel.getMaxWeightedPath(9))
