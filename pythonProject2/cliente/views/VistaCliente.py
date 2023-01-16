from PyQt5 import QtCore
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton

from abbonamento.views.VistaAbbonamento import VistaAbbonamento
from cliente.controller.ControlloreCliente import ControlloreCliente
from cliente.views.VistaModificaCliente import VistaModificaCliente
from cliente.views.VistaIngresso import VistaIngresso


class VistaCliente(QWidget):
    def __init__(self, cliente, elimina_cliente, callback, controller_lista, parent=None):
        super(VistaCliente, self).__init__(parent)
        self.cliente = cliente
        self.controller = ControlloreCliente(cliente)
        self.elimina_cliente = elimina_cliente
        self.callback = callback
        self.controller_lista = controller_lista

        v_layout = QVBoxLayout()

        label_nome = QLabel(self.controller.get_nome_cliente() + " " + self.controller.get_cognome_cliente())
        label_nome.setAlignment(QtCore.Qt.AlignCenter)
        font_nome = label_nome.font()
        font_nome.setPointSize(25)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        v_layout.addWidget(self.get_label_info("Codice Fiscale", self.controller.get_cf_cliente()))
        v_layout.addWidget(self.get_label_info("Indirizzo", self.controller.get_indirizzo_cliente()))
        v_layout.addWidget(self.get_label_info("Email", self.controller.get_email_cliente()))
        v_layout.addWidget(self.get_label_info("Telefono", self.controller.get_telefono_cliente()))
        v_layout.addWidget(self.get_label_info("Età", self.controller.get_eta_cliente()))

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_abbonamento = QPushButton("Abbonamento")
        btn_abbonamento.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        btn_abbonamento.setStyleSheet("border: 2px solid;" +
                                  "border-radius: 11px;" +
                                  "font-size: 17px;" +
                                      "font-weight: bold;" +
                                  "color: 'black'"
                                  )
        btn_abbonamento.clicked.connect(self.check_abbonamento)
        v_layout.addWidget(btn_abbonamento)

        v_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ingresso = QPushButton("Ingresso")
        btn_ingresso.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        btn_ingresso.setStyleSheet("border: 2px solid;" +
                                  "border-radius: 11px;" +
                                  "font-size: 17px;" +
                                   "font-weight: bold;" +
                                  "color: 'black'"
                                  )
        btn_ingresso.clicked.connect(self.check_ingresso)
        v_layout.addWidget(btn_ingresso)

        v_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_elimina = QPushButton("Elimina")
        btn_elimina.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        btn_elimina.setStyleSheet("border: 2px solid;" +
                                  "border-radius: 11px;" +
                                  "font-size: 17px;" +
                                  "font-weight: bold;" +
                                  "color: 'black'"
                                  )
        btn_elimina.clicked.connect(self.elimina_cliente_click)
        v_layout.addWidget(btn_elimina)

        v_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_modifica = QPushButton("Modifica")
        btn_modifica.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        btn_modifica.setStyleSheet("border: 2px solid;" +
                                  "border-radius: 11px;" +
                                  "font-size: 17px;" +
                                   "font-weight: bold;" +
                                  "color: 'black'"
                                  )
        btn_modifica.clicked.connect(self.modifica_cliente_click)
        v_layout.addWidget(btn_modifica)

        self.setLayout(v_layout)
        self.setWindowTitle(self.controller.get_nome_cliente() + " " + self.controller.get_cognome_cliente())

    def get_label_info(self, testo, valore):
        current_label = QLabel("[{}] {}".format(testo, valore))
        current_font = current_label.font()
        current_font.setPointSize(17)
        current_label.setFont(current_font)
        return current_label

    def check_abbonamento(self):
        self.vista_abbonamento = VistaAbbonamento(self.controller.get_abbonamento_cliente(),
                                                  self.controller.aggiungi_nuovo_abbonamento_cliente)
        self.vista_abbonamento.show()

    def check_ingresso(self):
        self.vista_ingresso = VistaIngresso(self.cliente)
        self.vista_ingresso.show()
        pass

    def elimina_cliente_click(self):
        self.elimina_cliente(self.controller.get_id_cliente())
        self.callback()
        self.close()

    def modifica_cliente_click(self):
        self.modifica = VistaModificaCliente(self.controller_lista, self.callback, self.cliente)
        self.modifica.show()
