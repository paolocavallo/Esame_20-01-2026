import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_create_graph(self, e):
        self._model.load_artists_with_min_albums(int(self._view.txtNumAlbumMin.value))
        nodi, archi= self._model.build_graph()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Grafo creato: {nodi} nodi (artisti), {archi} archi"))
        self._view.update_page()
        self._view.ddArtist.disabled = False
        dizionario = self._model.populate_dd()
        for chiave in dizionario:
            self._view.ddArtist.options.append(ft.dropdown.Option(key = chiave, text=dizionario[chiave].name))
        self._view.update_page()


    def handle_connected_artists(self, e):
        self._view.ddArtist.disabled = False
        dizionario = self._model.populate_dd()
        for chiave in dizionario:
            self._view.ddArtist.options.append(ft.dropdown.Option(key=chiave, text=dizionario[chiave].name))
        self._view.update_page()
        self._view.btnArtistsConnected.disabled = False
        vicini = self._model.collegamenti_artisti(self._view.ddArtist.value)
        self._view.txt_result.controls.clear()
        for vicino in vicini:
            self._view.txt_result.controls.append(ft.Text(f"{vicino}"))
        self._view.update_page()



