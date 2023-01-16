from unittest import TestCase

from attivita.model.Attivita import Attivita
from cliente.model.Cliente import Cliente
from listaprenotazioni.controller.ControlloreListaPrenotazioni import ControlloreListaPrenotazioni
from prenotazione.model.Prenotazione import Prenotazione


class TestPrenotazioni(TestCase):

    #inserisce ed elimina una prenotazione
    def test_inserisci_elimina_prenotazione(self):
        self.attivita = Attivita("Boxe", "Corso", 20)
        self.cliente = Cliente("lucaverdi", "luca", "verdi", "vrdlcu00p26a485x", "via 45", "lucaverdi@live.it",
                               "3298272625", "31")
        self.controllore_lista = ControlloreListaPrenotazioni()
        self.controllore_lista.aggiungi_prenotazione(Prenotazione("lucaverdi", self.cliente,
                                                                  self.attivita,
                                                                  "22/09/2023"))
        self.assertTrue(self.controllore_lista.get_lista_delle_prenotazioni())

