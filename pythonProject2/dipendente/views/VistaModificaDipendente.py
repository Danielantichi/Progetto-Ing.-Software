from PyQt5 import QtCore
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSpacerItem, QSizePolicy, QPushButton, QLabel, QLineEdit, QMessageBox, \
    QComboBox

from dipendente.model.Dipendente import Dipendente


class VistaModificaDipendente(QWidget):
    def __init__(self, controller, callback, dipendente):
        super(VistaModificaDipendente, self).__init__()
        self.controller = controller
        self.callback = callback
        self.dipendente = dipendente

        self.v_layout = QVBoxLayout()
        self.d = {'password': self.dipendente.password,
                  'nome': self.dipendente.nome,
                  'cognome': self.dipendente.cognome,
                  'cf': self.dipendente.cf,
                  'data_n': self.dipendente.datanascita,
                  'luogo_n': self.dipendente.luogonascita,
                  'email': self.dipendente.email,
                  'telefono': self.dipendente.telefono}
        self.qlines = {}
        self.add_info_text("password", "Password")
        self.add_info_text("nome", "Nome")
        self.add_info_text("cognome", "Cognome")
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
        btn_ok.clicked.connect(self.modifica_dipendente)
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.resize(600, 500)
        self.setWindowTitle("Modifica " + dipendente.nome + " " + dipendente.cognome)

    def add_info_text(self, key, label):
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self.d[key])
        self.qlines[key] = current_text
        self.v_layout.addWidget(current_text)

    def modifica_dipendente(self):
        for value in self.qlines.values():
            if value.text() == "":
                QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste.', QMessageBox.Ok, QMessageBox.Ok)
                return
        self.controller.modifica_dipendente_by_id(self.dipendente.id, Dipendente(
            (self.qlines["nome"].text()+self.qlines["cognome"].text()).lower(),
            self.qlines["password"].text(),
            self.qlines["nome"].text(),
            self.qlines["cognome"].text(),
            self.qlines["datanascita"].text(),
            self.qlines["luogonascita"].text(),
            self.qlines["cf"].text(),
            self.qlines["telefono"].text(),
            self.qlines["email"].text(),
            self.converti_in_testo())
        )
        self.callback()
        self.close()

    def converti_in_testo(self):
        ctext = self.scelta.currentText()
        return ctext
