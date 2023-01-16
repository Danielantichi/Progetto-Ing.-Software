import json
import pickle
import os.path

from attivita.model.Attivita import Attivita


class ListaAttivita():

    def __init__(self):
        super(ListaAttivita, self).__init__()
        self.lista_attivita = []

        if os.path.isfile('listaattivita/data/lista_attivita_salvata.pickle'):
            with open('listaattivita/data/lista_attivita_salvata.pickle', 'rb') as f:
                self.lista_attivita = pickle.load(f)
        else:
            with open('listaattivita/data/lista_attivita_iniziali.json') as f:
                lista_attivita_iniziali = json.load(f)
            for attivita_iniziale in lista_attivita_iniziali:
                self.aggiungi_attivita(Attivita(attivita_iniziale["nome"],attivita_iniziale["tipo"],
                                                attivita_iniziale["prezzo"]))

    def aggiungi_attivita(self, attivita):
        self.lista_attivita.append(attivita)

    def get_attivita_by_index(self, index):
        return self.lista_attivita[index]

    def get_lista_attivita(self):
        return self.lista_attivita

    def save_data(self):
        with open('listaattivita/data/lista_attivita_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_attivita, handle, pickle.HIGHEST_PROTOCOL)