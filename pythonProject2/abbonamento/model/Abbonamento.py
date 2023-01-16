import json
import time
from datetime import timedelta, datetime


class Abbonamento():
    def __init__(self, tipo):
        self.tipo = tipo
        self.lista_tipi = []
        with open('abbonamento/data/lista_abbonamenti.json') as f:
            self.lista_tipi = json.load(f)
        for i in self.lista_tipi:
            if i["tipo"] == self.tipo:
                self.prezzo = i["prezzo"]
                self.scadenza = datetime.today() + timedelta(days=i["durata"])

    def is_scaduto(self):
        timestamp = int(time.time())
        data = datetime.fromtimestamp(timestamp)
        print(self.scadenza)
        if data > self.scadenza:
            return True
        else:
            return False
