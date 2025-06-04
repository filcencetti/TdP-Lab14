import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDDstores(self):
        myValuesDD = list(map(lambda x: ft.dropdown.Option(data=x, key=x.store_id, on_click=self.read_DD_value), self._model.getStores()))
        self._view._ddStore.options = myValuesDD

    def handleCreaGrafo(self, e):
        if self._view._ddStore is None or self._view._ddStore == "":
            self._view.create_alert()

        self._model.buildGraph(self.store,self._view._txtIntK.value)


    def handleCerca(self, e):
        pass

    def handleRicorsione(self, e):
        pass

    def read_DD_value(self, e):
        self.store = e.control.data
