class ControlloreAttivita():
    def __init__(self, attivita):
        self.model = attivita

    def get_nome_attivita(self):
        return self.model.nome

    def get_tipo_attivita(self):
        return self.model.tipo

    def get_prezzo_attivita(self):
        return "{}".format(self.model.prezzo)

    def get_attivita_disponibile(self):
        if self.model.is_disponibile():
            return "Disponibile"
        else:
            return "Non Disponibile"
