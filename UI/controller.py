import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDDstores(self):
        myValuesDD = list(map(lambda x: ft.dropdown.Option(data=x, key=x.store_id, on_click=self.read_DDStores_value), self._model.getStores()))
        self._view._ddStore.options = myValuesDD

    def handleCreaGrafo(self, e):
        if self._view._ddStore.value is None or self._view._ddStore.value == "":
            self._view.create_alert(f"Scegliere un negozio!!!")
            self._view.update_page()
            return

        if self._view._txtIntK.value == "":
            self._view.create_alert(f"Scegliere un negozio!!!")
            self._view.update_page()
            return

        try:
            intK = int(self._view._txtIntK.value)
        except:
            self._view.create_alert(f"Inserire un valore numerico!!!")
            self._view.update_page()
            return
        self._view.txt_result.controls.clear()
        self._model.buildGraph(self.store.store_id,intK)
        self._view.txt_result.controls.append(ft.Text(f"Grafi creato correttamente \n"
                                              f"Numero di nodi: {self._model._graph.number_of_nodes()}\n"
                                              f"Numero di archi: {self._model._graph.number_of_edges()}"))
        self._view._ddNode.disabled = False
        self._view._btnCerca.disabled = False
        self.fillDDNode()
        self._view.update_page()

    def fillDDNode(self):
        myValuesDD = list(map(lambda x: ft.dropdown.Option(data=x, key=x.order_id, on_click=self.read_DDNode_value),self._model._graph.nodes()))
        self._view._ddNode.options = myValuesDD

    def handleCerca(self, e):
        longest_path = self._model.getPath(int(self._view._ddNode.value))
        self._view.txt_result.controls.append(ft.Text(f"Nodo di partenza: {self._view._ddNode.value}"))
        for i in range(len(longest_path)):
            self._view.txt_result.controls.append(ft.Text(f"{longest_path[i]}"))
        self._view._btnRicorsione.disabled = False
        self._view.update_page()

    def handleRicorsione(self, e):
        self._model.getMaxWeightedPath(int(self._view._ddNode.value))
        self._view.txt_result.controls.append(ft.Text(f"Nodo di partenza: {self._view._ddNode.value}"))
        for i in range(len(self._model._bestPath)):
            self._view.txt_result.controls.append(ft.Text(f"{self._model._bestPath[i]}"))
        self._view.txt_result.controls.append(ft.Text(f"Peso del percorso {self._model._bestScore}"))
        self._view.update_page()


    def read_DDStores_value(self, e):
        self.store = e.control.data

    def read_DDNode_value(self, e):
        self.selected_node = e.control.data
