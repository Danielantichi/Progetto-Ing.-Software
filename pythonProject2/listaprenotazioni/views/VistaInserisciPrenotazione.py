import os
import pickle

from PyQt5 import QtCore
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QCursor
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QComboBox, QSpacerItem, QSizePolicy, QPushButton, \
    QMessageBox

from listaentrate.controller.ControlloreListaEntrate import ControlloreListaEntrate
from prenotazione.model.Prenotazione import Prenotazione


class VistaInserisciPrenotazione(QWidget):
    def __init__(self, controller, callback):
        super(VistaInserisciPrenotazione, self).__init__(parent=None)
        self.controller = controller
        self.controllerentrate = ControlloreListaEntrate()
        self.callback = callback

        v_layout = QVBoxLayout()
        v_layout.addWidget(QLabel("Data (dd/MM/yyyy)"))
        self.text_data = QLineEdit(self)
        v_layout.addWidget(self.text_data)

        self.combo_clienti = QComboBox()
        self.comboclienti_model = QStandardItemModel(self.combo_clienti)
        if os.path.isfile('listaclienti/data/lista_clienti_salvata.pickle'):
            with open('listaclienti/data/lista_clienti_salvata.pickle', 'rb') as f:
                self.lista_clienti_salvata = pickle.load(f)
            self.lista_clienti_abbonati = [c for c in self.lista_clienti_salvata if c.get_abbonamento()]
            for cliente in self.lista_clienti_abbonati:
                item = QStandardItem()
                item.setText(cliente.nome + " " + cliente.cognome)
                item.setEditable(False)
                font = item.font()
                font.setPointSize(18)
                item.setFont(font)
                self.comboclienti_model.appendRow(item)
            self.combo_clienti.setModel(self.comboclienti_model)
        v_layout.addWidget(QLabel("Cliente"))
        v_layout.addWidget(self.combo_clienti)

        self.combo_attivita = QComboBox()
        self.comboattivita_model = QStandardItemModel(self.combo_attivita)
        if os.path.isfile('listaattivita/data/lista_attivita_salvata.pickle'):
            with open('listaattivita/data/lista_attivita_salvata.pickle', 'rb') as f:
                self.lista_attivita_salvata = pickle.load(f)
            self.lista_attivita_disponibili = []
            for a in self.lista_attivita_salvata:
                if a.is_disponibile():
                    self.lista_attivita_disponibili.append(a)
            for attivita in self.lista_attivita_disponibili:
                item = QStandardItem()
                item.setText(attivita.nome)
                item.setEditable(False)
                font = item.font()
                font.setPointSize(18)
                item.setFont(font)
                self.comboattivita_model.appendRow(item)
            self.combo_attivita.setModel(self.comboattivita_model)
        v_layout.addWidget(QLabel("Attivita"))
        v_layout.addWidget(self.combo_attivita)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        btn_ok.setStyleSheet("border: 2px solid;" +
                                  "border-radius: 11px;" +
                                  "font-size: 15px;" +
                                    "font-weight: bold;" +
                                  "color: 'black'"
                                  )
        btn_ok.clicked.connect(self.add_prenotazione)
        v_layout.addWidget(btn_ok)

        self.setLayout(v_layout)
        self.setWindowTitle('Nuova Prenotazione')

    def add_prenotazione(self):
        data = self.text_data.text()
        cliente = self.lista_clienti_abbonati[self.combo_clienti.currentIndex()]
        attivita = self.lista_attivita_disponibili[self.combo_attivita.currentIndex()]
        if data == "" or not cliente or not attivita:
            QMessageBox(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste', QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.controller.aggiungi_prenotazione(Prenotazione((cliente.cognome+cliente.nome).lower(), cliente, attivita, data))
            for a in self.lista_attivita_salvata:
                if a.nome == attivita.nome:
                    a.prenota()
            self.controllerentrate.aggiungi_entrata(attivita.nome, attivita.prezzo)
            with open('listaattivita/data/lista_attivita_salvata.pickle', 'wb') as f:
                pickle.dump(self.lista_attivita_salvata, f, pickle.HIGHEST_PROTOCOL)
            self.callback()
            self.close()
