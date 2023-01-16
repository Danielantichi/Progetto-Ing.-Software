from unittest import TestCase

from abbonamento.model.Abbonamento import Abbonamento
from cliente.controller.ControlloreCliente import ControlloreCliente
from cliente.model.Cliente import Cliente
from listaclienti.controller.ControlloreListaClienti import ControlloreListaClienti


class TestCliente(TestCase):
    #aggiunge un abbonamento
    def test_aggiungi_abbonamento(self):
        self.cliente = Cliente("lucaverdi", "luca", "verdi", "vrdlcu00p26a485x", "via 45", "lucaverdi@live.it",
                               "3298272625", "31")
        self.assertIsNone(self.cliente.abbonamento)
        self.cliente.add_abbonamento(Abbonamento)
        self.assertIsNotNone(self.cliente.abbonamento)

    #inserisce e rimuove ingressi
    def test_modifica_ingressi(self):
        self.cliente = Cliente("lucaverdi", "luca", "verdi", "vrdlcu00p26a485x", "via 45", "lucaverdi@live.it",
                               "3298272625", "31")
        self.assertEqual(self.cliente.ingressi, 0, "Ingressi diversi da 0")
        self.controllorecliente = ControlloreCliente(self.cliente)
        self.controllorecliente.add_ingresso()
        self.controllorecliente.add_ingresso()
        self.assertEqual(self.cliente.ingressi, 2, "Non è stato inserito alcun ingresso")
        self.controllorecliente.rimuovi_ingresso()
        self.assertEqual(self.cliente.ingressi, 1, "Non è stato rimosso alcun ingresso")

    #inserisce ed elimina un cliente
    def test_inserisci_ed_elimina_cliente(self):
        self.cliente = Cliente("lucaverdi", "luca", "verdi", "vrdlcu00p26a485x", "via 45", "lucaverdi@live.it",
                               "3298272625", "31")
        self.controllore_lista = ControlloreListaClienti()
        self.controllore_lista.aggiungi_cliente(self.cliente)
        self.assertTrue(self.controllore_lista.get_lista_dei_clienti())
        self.controllore = ControlloreCliente(self.cliente)
        self.controllore_lista.elimina_cliente_by_id(self.controllore.get_id_cliente())
        self.assertFalse(self.controllore_lista.get_lista_dei_clienti())



