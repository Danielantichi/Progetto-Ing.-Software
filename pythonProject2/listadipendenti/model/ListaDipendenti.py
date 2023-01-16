import json
import os
import pickle

from dipendente.model.Dipendente import Dipendente


class ListaDipendenti():
    def __init__(self):
        super(ListaDipendenti, self).__init__()
        self.lista_dipendenti = []

        if os.path.isfile('listadipendenti/data/lista_dipendenti_salvata.pickle'):
            with open('listadipendenti/data/lista_dipendenti_salvata.pickle', 'rb') as f:
                self.lista_dipendenti = pickle.load(f)
        with open('listadipendenti/data/amministratore.json') as f:
            lista_amministratori = json.load(f)
            for amministratore in lista_amministratori:
                self.aggiungi_dipendente(Dipendente(amministratore["id"], amministratore["password"],
                                                    amministratore["nome"], amministratore["cognome"],
                                                    amministratore["datanascita"], amministratore["luogonascita"],
                                                    amministratore["cf"], amministratore["telefono"],
                                                    amministratore["email"],amministratore["ruolo"], ))

    def modifica_dipendente_by_id(self, id, dipendente):
        for i in self.lista_dipendenti:
            if i.id == id:
                self.lista_dipendenti.remove(i)
        self.lista_dipendenti.append(dipendente)
        self.save_data()


    def aggiungi_dipendente(self, dipendente):
        self.lista_dipendenti.append(dipendente)

    def rimuovi_dipendente_by_id(self, id):
        def is_selected_dipendente(dipendente):
            if dipendente.id == id:
                return True
            return False
        self.lista_dipendenti.remove(list(filter(is_selected_dipendente, self.lista_dipendenti))[0])

    def get_dipendente_by_index(self, index):
        return self.lista_dipendenti[index]

    def get_lista_dipendenti(self):
        return self.lista_dipendenti

    def save_data(self):
        self.temp_lista_dipendenti = []
        for dipendente in self.lista_dipendenti:
            if dipendente.ruolo != "AMMINISTRATORE":
                self.temp_lista_dipendenti.append(dipendente)
        with open('listadipendenti/data/lista_dipendenti_salvata.pickle', 'wb') as handle:
            pickle.dump(self.temp_lista_dipendenti, handle, pickle.HIGHEST_PROTOCOL)