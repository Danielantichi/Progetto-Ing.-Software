import os
import pickle


class ListaEntrate():
    def __init__(self):
        super(ListaEntrate, self).__init__()
        self.lista_entrate = []
        if os.path.isfile('listaentrate/data/lista_entrate_salvata.pickle'):
            with open('listaentrate/data/lista_entrate_salvata.pickle', 'rb') as f:
                self.lista_entrate = pickle.load(f)

    def rimuovi_entrata_by_attivita(self, attivita):
        for entrata in self.lista_entrate:
            if entrata.attivita == attivita:
                self.lista_entrate.remove(entrata)
                return True
        return False

    def aggiungi_entrata(self, entrata):
        self.lista_entrate.append(entrata)
        self.save_data()

    def get_lista_entrate(self):
        return self.lista_entrate

    def get_entrata_by_index(self, index):
        return self.lista_entrate[index]

    def save_data(self):
        with open('listaentrate/data/lista_entrate_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_entrate, handle, pickle.HIGHEST_PROTOCOL)
