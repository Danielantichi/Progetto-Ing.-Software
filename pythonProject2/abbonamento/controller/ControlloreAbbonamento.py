class ControlloreAbbonamento():
    def __init__(self, abbonamento):
        self.model = abbonamento

    def is_abbonato(self):
        return self.model is not None

    def get_scadenza_string(self):
        scadenza_data = self.model.scadenza
        return "Scadenza {}/{}/{}".format(scadenza_data.day, scadenza_data.month, scadenza_data.year)
