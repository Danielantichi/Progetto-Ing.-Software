class Attivita():

    def __init__(self, nome, tipo, prezzo):
        super(Attivita, self).__init__()
        self.nome = nome
        self.tipo = tipo
        self.prezzo = prezzo
        self.disponibile = True

    def is_disponibile(self):
        return self.disponibile

    def prenota(self):
        self.disponibile = False