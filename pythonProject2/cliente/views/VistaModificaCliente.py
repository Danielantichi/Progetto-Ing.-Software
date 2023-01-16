from PyQt5 import QtCore
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSpacerItem, QSizePolicy, QPushButton, QLabel, QLineEdit, QMessageBox

from cliente.model.Cliente import Cliente


class VistaModificaCliente(QWidget):
    def __init__(self, controller, callback, cliente):
        super(VistaModificaCliente, self).__init__()
        self.controller = controller
        self.callback = callback
        self.cliente = cliente

        self.v_layout = QVBoxLayout()
        self.d = {'nome': self.cliente.nome,
                  'cognome': self.cliente.cognome,
                  'cf': self.cliente.cf,
                  'indirizzo': self.cliente.indirizzo,
                  'email': self.cliente.email,
                  'telefono': self.cliente.telefono,
                  'eta': self.cliente.eta}
        self.info = {}
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
                                      "font-size: 17px;" +
                                        "font-weight: bold;" +
                                      "color: 'black'"
                                      )
        btn_ok.clicked.connect(self.modifica_cliente)
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.resize(600, 400)
        self.setWindowTitle("Modifica " + cliente.nome + " " + cliente.cognome)

    def add_info_text(self, nome, label):
        self.v_layout.addWidget(QLabel(label))
        current_text_edit = QLineEdit(self.d[nome])
        self.info[nome] = current_text_edit
        self.v_layout.addWidget(current_text_edit)

    def modifica_cliente(self):
        for value in self.info.values():
            if value.text() == "":
                QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste.',
                                     QMessageBox.Ok, QMessageBox.Ok)
                return
        self.controller.modifica_cliente_by_id(self.cliente.id, Cliente((self.info["nome"].text()+self.info["cognome"].text()).lower(),
                                                 self.info["nome"].text(), self.info["cognome"].text(),
                                                 self.info["cf"].text(), self.info["indirizzo"].text(),
                                                 self.info["email"].text(), self.info["telefono"].text(),
                                                 self.info["eta"].text()))
        self.callback()
        self.close()
