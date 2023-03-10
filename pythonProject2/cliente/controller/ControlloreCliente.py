class ControlloreCliente():
    def __init__(self, cliente):
        self.model = cliente

    def get_id_cliente(self):
        return self.model.id

    def get_nome_cliente(self):
        return self.model.nome

    def get_cognome_cliente(self):
        return self.model.cognome

    def get_cf_cliente(self):
        return self.model.cf

    def get_indirizzo_cliente(self):
        return self.model.indirizzo

    def get_email_cliente(self):
        return self.model.email

    def get_telefono_cliente(self):
        return self.model.telefono

    def get_eta_cliente(self):
        return self.model.eta

    def get_abbonamento_cliente(self):
        return self.model.get_abbonamento()

    def get_ingressi_cliente(self):
        return self.model.ingressi

    def aggiungi_nuovo_abbonamento_cliente(self, abbonamento):
        self.model.add_abbonamento(abbonamento)

    def add_ingresso(self):
        self.model.ingressi += 1

    def rimuovi_ingresso(self):
        if self.model.ingressi == 0:
            return
        self.model.ingressi -= 1
