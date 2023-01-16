import json
import os
import pickle

from dipendente.model.Dipendente import Dipendente
from homee.views.VistaHome import VistaHome


class Login():
    def __init__(self):
        super(Login, self).__init__()
        self.lista_dipendenti = []

        if os.path.isfile('listadipendenti/data/lista_dipendenti_salvata.pickle'):
            with open('listadipendenti/data/lista_dipendenti_salvata.pickle', 'rb') as f:
                self.lista_dipendenti = pickle.load(f)
        with open('listadipendenti/data/amministratore.json') as f:
            lista_amministratori = json.load(f)
            for amministratore in lista_amministratori:
                self.lista_dipendenti.append(Dipendente(amministratore["id"], amministratore["password"],
                                                    amministratore["nome"], amministratore["cognome"],
                                                    amministratore["datanascita"], amministratore["luogonascita"],
                                                    amministratore["cf"], amministratore["telefono"],
                                                    amministratore["email"], amministratore["ruolo"], ))

    def login_dipentente(self, id, password):
        for a in self.lista_dipendenti:
            if id == a.id and password == a.password:
                for a in self.lista_dipendenti:
                    if a.id == id and a.password == password:
                        with open('login/data/dipendentelogged.pickle', 'wb') as handle:
                            pickle.dump(a, handle, pickle.HIGHEST_PROTOCOL)
                        self.vista_home = VistaHome()
                        self.vista_home.show()
                return True
        return False
