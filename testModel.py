from model.model import Model

mymodel = Model()
mymodel.buildGraph(2,5)
print(len(mymodel.getPath(10)))
