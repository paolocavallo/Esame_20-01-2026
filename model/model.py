import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._artists_list = []
        self.artists_dict = {}
        self.lista = []
        self.load_all_artists()

    def load_all_artists(self):
        self._artists_list = DAO.get_all_artists()
        print(f"Artisti: {self._artists_list}")

    def load_artists_with_min_albums(self, min_albums):
        self._graph.clear()
        lista_artisti = DAO().get_nodes(min_albums)
        for artist in self._artists_list:
            self.artists_dict[artist.id] = artist
        for artista in lista_artisti:
            self.lista.append(artista['id'])
        print(self.lista)
        self._graph.add_nodes_from(self.lista)
        print(len(self.lista))




    def build_graph(self):
        self._graph.clear()
        lista_edges = DAO().get_connessioni()
        for arco in lista_edges:
            if arco['artista1'] in self.lista and arco["artista2"] in self.lista:
                self._graph.add_edge(arco['artista1'], arco['artista2'], weight = arco['peso'])
        num_nodi = self._graph.number_of_nodes()
        num_archi = self._graph.number_of_edges()
        #print(num_nodi)
        #print(num_archi)
        return num_nodi, num_archi

    def populate_dd(self):
        dict_artisti = {}
        for artista in self.lista:
            dict_artisti[artista] = self.artists_dict[artista]
        return dict_artisti

    def collegamenti_artisti(self, codice):
        self._graph.neighbors(codice)


