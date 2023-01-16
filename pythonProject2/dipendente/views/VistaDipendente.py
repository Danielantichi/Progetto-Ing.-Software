from PyQt5 import QtCore
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton

from dipendente.controller.ControlloreDipendente import ControlloreDipendente
from dipendente.views.VistaModificaDipendente import VistaModificaDipendente


class VistaDipendente(QWidget):
    def __init__(self, dipendente, elimina_dipendente, callback, controller_lista, parent=None):
        super(VistaDipendente, self).__init__(parent)
        self.controller_lista = controller_lista
        self.controller = ControlloreDipendente(dipendente)
        self.elimina_dipendente = elimina_dipendente
        self.callback = callback
        self.dipendente = dipendente
        v_layout = QVBoxLayout()

        label_nome = QLabel(self.controller.get_nome_dipendente() + " " + self.controller.get_cognome_dipendente())
        label_nome.setAlignment(QtCore.Qt.AlignCenter)
        font_nome = label_nome.font()
        font_nome.setPointSize(25)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        v_layout.addWidget(self.get_info("Codice Fiscale: {}".format(self.controller.get_cf_dipendente())))
        v_layout.addWidget(self.get_info("Data Nascita: {}".format(self.controller.get_datanascita_dipendente())))
        v_layout.addWidget(self.get_info("Luogo Nascita: {}".format(self.controller.get_luogonascita_dipendente())))
        v_layout.addWidget(self.get_info("Email: {}".format(self.controller.get_email_dipendente())))
        v_layout.addWidget(self.get_info("Telefono: {}".format(self.controller.get_telefono_dipendente())))
        v_layout.addWidget(self.get_info("Ruolo: {}".format(self.controller.get_ruolo_dipendente())))
        v_layout.addWidget(self.get_info("Password: {}".format(self.controller.get_password_dipendente())))
        v_layout.addWidget(self.get_info("Id: {}".format(self.controller.get_id_dipendente())))

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_elimina = QPushButton("Elimina")
        btn_elimina.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        btn_elimina.setStyleSheet("border: 2px solid;" +
                                  "border-radius: 11px;" +
                                  "font-size: 17px;" +
                                  "font-weight: bold;" +
                                  "color: 'black'"
                                  )
        btn_elimina.clicked.connect(self.elimina_dipendente_click)
        v_layout.addWidget(btn_elimina)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_modifica = QPushButton("Modifica")
        btn_modifica.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        btn_modifica.setStyleSheet("border: 2px solid;" +
                                  "border-radius: 11px;" +
                                  "font-size: 17px;" +
                                   "font-weight: bold;" +
                                  "color: 'black'"
                                  )
        btn_modifica.clicked.connect(self.modifica_dipendente_click)
        v_layout.addWidget(btn_modifica)

        self.setLayout(v_layout)
        self.setWindowTitle(self.controller.get_nome_dipendente())

    def get_info(self, text):
        label = QLabel(text)
        font = label.font()
        font.setPointSize(17)
        label.setFont(font)
        return label

    def elimina_dipendente_click(self):
        self.elimina_dipendente(self.controller.get_id_dipendente())
        self.callback()
        self.close()

    def modifica_dipendente_click(self):
        self.modifica_dipendente = VistaModificaDipendente(self.controller_lista, self.callback, self.dipendente)
        self.modifica_dipendente.show()
