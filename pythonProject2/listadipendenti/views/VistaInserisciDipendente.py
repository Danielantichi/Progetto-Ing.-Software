from datetime import datetime

from PyQt5 import QtCore
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QSpacerItem, QSizePolicy, QPushButton, QMessageBox, \
    QComboBox

from dipendente.model.Dipendente import Dipendente


class VistaInserisciDipendente(QWidget):
    def __init__(self, controller, callback):
        super(VistaInserisciDipendente, self).__init__()
        self.controller = controller
        self.callback = callback

        self.v_layout = QVBoxLayout()

        self.qlines = {}
        self.add_info_text("nome", "Nome")
        self.add_info_text("cognome", "Cognome")
        self.add_info_text("password", "Password")
        self.add_info_text("cf", "Codice Fiscale")
        self.add_info_text("data_n", "Data di nascita (dd/MM/yyyy)")
        self.add_info_text("luogo_n", "Luogo di nascita")
        self.add_info_text("email", "Email")
        self.add_info_text("telefono", "Telefono")

        self.v_layout.addWidget(QLabel("Ruolo"))
        self.scelta = QComboBox(self)
        self.scelta.addItem("AMMINISTRATORE")
        self.scelta.addItem("PERSONAL TRAINER")
        self.scelta.addItem("CASSIERE")
        self.scelta.addItem("RECEPTIONIST")
        self.v_layout.addWidget(self.scelta)

        self.v_layout.addItem(QSpacerItem(40, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        btn_ok.setStyleSheet("border: 2px solid;" +
                                  "border-radius: 11px;" +
                                  "font-size: 15px;" +
                                    "font-weight: bold;" +
                                  "color: 'black'"
                                  )
        btn_ok.clicked.connect(self.add_dipendente)
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Nuovo Dipendente")

    def add_info_text(self, nome, label):
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qlines[nome] = current_text
        self.v_layout.addWidget(current_text)

    def add_dipendente(self):
        for value in self.qlines.values():
            if value.text() == "":
                QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste.',
                                     QMessageBox.Ok, QMessageBox.Ok)
                return
        try:
            data = datetime.strptime(self.qlines["data_n"].text(), '%d/%m/%Y')
            self.controller.aggiungi_dipendente(Dipendente(
                (self.qlines["nome"].text()+self.qlines["cognome"].text()).lower(),
                self.qlines["password"].text(),
                self.qlines["nome"].text(),
                self.qlines["cognome"].text(),
                data,
                self.qlines["luogo_n"].text(),
                self.qlines["cf"].text(),
                self.qlines["telefono"].text(),
                self.qlines["email"].text(),
                self.converti_in_testo())
            )
            self.callback()
            self.close()
        except:
            QMessageBox.critical(self, 'Errore', 'Inserisci la data nel formato richiesto: dd/MM/yyyy', QMessageBox.Ok,
                                 QMessageBox.Ok)

    def converti_in_testo(self):
        ctext = self.scelta.currentText()
        return ctext
