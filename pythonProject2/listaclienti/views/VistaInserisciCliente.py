from PyQt5 import QtCore
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSpacerItem, QSizePolicy, QPushButton, QLabel, QLineEdit, QMessageBox

from cliente.model.Cliente import Cliente


class VistaInserisciCliente(QWidget):
    def __init__(self, controller, callback):
        super(VistaInserisciCliente, self).__init__()
        self.controller = controller
        self.callback = callback
        self.info = {}

        self.v_layout = QVBoxLayout()

        self.add_info_text("nome", "Nome")
        self.add_info_text("cognome", "Cognome")
        self.add_info_text("cf", "Codice Fiscale")
        self.add_info_text("indirizzo", "Indirizzo")
        self.add_info_text("email", "Email")
        self.add_info_text("telefono", "Telefono")
        self.add_info_text("eta", "Età")

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        btn_ok.setStyleSheet("border: 2px solid;" +
                                      "border-radius: 11px;" +
                                      "font-size: 15px;" +
                                        "font-weight: bold;" +
                                      "color: 'black'"
                                      )
        btn_ok.clicked.connect(self.add_cliente)
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Nuovo Cliente")

    def add_info_text(self, nome, label):
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.info[nome] = current_text
        self.v_layout.addWidget(current_text)

    def add_cliente(self):
        for value in self.info.values():
            if value.text() == "":
                QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste.',
                                     QMessageBox.Ok, QMessageBox.Ok)
                return
        self.controller.aggiungi_cliente(Cliente((self.info["nome"].text()+self.info["cognome"].text()).lower(),
                                                 self.info["nome"].text(), self.info["cognome"].text(),
                                                 self.info["cf"].text(), self.info["indirizzo"].text(),
                                                 self.info["email"].text(), self.info["telefono"].text(),
                                                 self.info["eta"].text()))
        self.callback()
        self.close()

