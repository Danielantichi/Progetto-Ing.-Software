from listaattivita.model.ListaAttivita import ListaAttivita


class ControlloreListaAttivita():

    def __init__(self):
        super(ControlloreListaAttivita, self).__init__()
        self.model = ListaAttivita()

    def get_lista_delle_attivita(self):
        return self.model.get_lista_attivita()

    def get_attivita_by_index(self, index):
        return self.model.get_attivita_by_index(index)

    def save_data(self):
        self.model.save_data()