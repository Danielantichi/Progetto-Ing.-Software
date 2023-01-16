import pickle

from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QLabel, QSpacerItem, QVBoxLayout

from listaattivita.views.VistaListaAttivita import VistaListaAttivita
from listaclienti.views.VistaListaCliente import VistaListaClienti
from listadipendenti.views.VistaListaDipendenti import VistaListaDipendenti
from listaentrate.views.VistaListaEntrate import VistaListaEntrate
from listaprenotazioni.views.VistaListaPrenotazioni import VistaListaPrenotazioni
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor


class VistaHome(QWidget):
    def __init__(self, parent=None):
        super(VistaHome, self).__init__(parent)
        self.lista_ruoli = []

        self.v_layout = QVBoxLayout()

        label_nome = QLabel("[HOME - PALESTRA]")
        label_nome.setAlignment(QtCore.Qt.AlignCenter)
        font_nome = label_nome.font()
        font_nome.setPointSize(25)
        label_nome.setStyleSheet("font-weight: bold; color: black")
        label_nome.setFont(font_nome)
        self.v_layout.addWidget(label_nome)

        self.v_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        grid_layout = QGridLayout()
        self.lista_ruoli.append("AMMINISTRATORE")
        self.lista_ruoli.append("PERSONAL TRAINER")

        if self.controlla_permessi(self.lista_ruoli):
            grid_layout.addWidget(self.get_generic_button("Lista Prenotazioni", self.go_lista_prenotazioni), 1, 1)
            grid_layout.addWidget(self.get_generic_button("Lista Clienti", self.go_lista_clienti), 0, 1)

        self.lista_ruoli.remove("PERSONAL TRAINER")
        self.lista_ruoli.append("RECEPTIONIST")
        if self.controlla_permessi(self.lista_ruoli):
            grid_layout.addWidget(self.get_generic_button("Lista Clienti", self.go_lista_clienti), 0, 1)
            grid_layout.addWidget(self.get_generic_button("Lista Prenotazioni", self.go_lista_prenotazioni), 1, 1)
            grid_layout.addWidget(self.get_generic_button("Lista Dipendenti", self.go_lista_dipendenti), 1, 0)

        self.lista_ruoli.remove("RECEPTIONIST")
        self.lista_ruoli.append("CASSIERE")
        if self.controlla_permessi(self.lista_ruoli):
            grid_layout.addWidget(self.get_generic_button("Lista Entrate", self.go_lista_entrate), 2, 0)
            grid_layout.addWidget(self.get_generic_button("Lista Attivita", self.go_lista_attivita), 0, 0)

        self.v_layout.addLayout(grid_layout)

        self.v_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        image = QPixmap("PalestraLogo.jpg")
        logo = QLabel()
        logo.setPixmap(image)
        logo.setAlignment(QtCore.Qt.AlignCenter)
        logo.setStyleSheet("margin-top: 50px;")
        logo.setStyleSheet("margin-bottom: 60px;")
        self.v_layout.addWidget(logo)

        self.setLayout(self.v_layout)
        self.resize(600, 450)
        self.setWindowTitle("Home Palestra")

    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        button.setStyleSheet("border: 2px solid;" +
                             "border-radius: 11px;" +
                             "font-size: 20px;" +
                             "font-weight: bold;" +
                             "color: 'black'")
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def go_lista_attivita(self):
        self.vista_lista_attivita = VistaListaAttivita()
        self.vista_lista_attivita.show()

    def go_lista_clienti(self):
        self.vista_lista_clienti = VistaListaClienti()
        self.vista_lista_clienti.show()

    def go_lista_dipendenti(self):
        self.vista_lista_dipendenti = VistaListaDipendenti()
        self.vista_lista_dipendenti.show()

    def go_lista_prenotazioni(self):
        self.vista_lista_prenotazioni = VistaListaPrenotazioni()
        self.vista_lista_prenotazioni.show()

    def go_lista_entrate(self):
        self.vista_lista_entrate = VistaListaEntrate()
        self.vista_lista_entrate.show()

    def controlla_permessi(self, lista_ruoli_permessi):
        with open('login/data/dipendentelogged.pickle', 'rb') as f:
            dipendente_logged = pickle.load(f)
        ruolo_logged = dipendente_logged.ruolo
        for ruolo in lista_ruoli_permessi:
            if ruolo == ruolo_logged:
                return True
        return False