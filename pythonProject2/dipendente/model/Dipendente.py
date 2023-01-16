class Dipendente():
    def __init__(self, id, password, nome, cognome, datanascita, luogonascita, cf, telefono, email, ruolo):
        super(Dipendente, self).__init__()
        self.id = id
        self.password = password
        self.nome = nome
        self.cognome = cognome
        self.datanascita = datanascita
        self.luogonascita = luogonascita
        self.cf = cf
        self.telefono = telefono
        self.email = email
        self.ruolo = ruolo
