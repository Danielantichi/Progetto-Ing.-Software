from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy

from attivita.controller.ControlloreAttivita import ControlloreAttivita


class VistaAttivita(QWidget):
    def __init__(self, attivita, parent=None):
        super(VistaAttivita, self).__init__(parent)
        self.controller = ControlloreAttivita(attivita)

        v_layout = QVBoxLayout()
        label_nome = QLabel(self.controller.get_nome_attivita())
        label_nome.setAlignment(QtCore.Qt.AlignCenter)
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        v_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        label_tipo = QLabel("[Tipo]   {}".format(self.controller.get_tipo_attivita()))
        label_tipo.setAlignment(QtCore.Qt.AlignCenter)
        font_tipo = label_tipo.font()
        font_tipo.setPointSize(15)
        label_tipo.setFont(font_tipo)
        v_layout.addWidget(label_tipo)

        v_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        label_prezzo = QLabel("[Prezzo]   {}€".format(self.controller.get_prezzo_attivita()))
        label_prezzo.setAlignment(QtCore.Qt.AlignCenter)
        font_prezzo = label_prezzo.font()
        font_prezzo.setPointSize(15)
        label_prezzo.setFont(font_prezzo)
        v_layout.addWidget(label_prezzo)

        v_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        label_disponibile = QLabel("[Disponibilità]   {}".format(self.controller.get_attivita_disponibile()))
        label_disponibile.setAlignment(QtCore.Qt.AlignCenter)
        font_disponibile = label_disponibile.font()
        font_disponibile.setPointSize(15)
        label_disponibile.setFont(font_disponibile)
        v_layout.addWidget(label_disponibile)

        self.setLayout(v_layout)
        self.resize(400, 200)
        self.setWindowTitle(attivita.nome)
