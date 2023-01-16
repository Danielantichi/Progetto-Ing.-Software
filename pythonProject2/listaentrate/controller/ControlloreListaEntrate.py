from entrata.model.Entrata import Entrata
from listaentrate.model.ListaEntrate import ListaEntrate


class ControlloreListaEntrate():
    def __init__(self):
        self.model = ListaEntrate()

    def elimina_entrata_by_attivita(self, attivita):
        return self.model.rimuovi_entrata_by_attivita(attivita)

    def aggiungi_entrata(self, nome, prezzo):
        entrata = Entrata(nome, prezzo)
        self.model.aggiungi_entrata(entrata)

    def get_lista_delle_entrate(self):
        return self.model.get_lista_entrate()

    def get_entrata_by_index(self, index):
        return self.model.get_entrata_by_index(index)

    def save_data(self):
        self.model.save_data()
