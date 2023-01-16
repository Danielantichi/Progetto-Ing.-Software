from PyQt5 import QtCore
from PyQt5.QtGui import QStandardItem, QStandardItemModel, QCursor
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSpacerItem, QSizePolicy, QListView

from cliente.controller.ControlloreCliente import ControlloreCliente
from listaentrate.controller.ControlloreListaEntrate import ControlloreListaEntrate


class VistaIngresso(QWidget):
    def __init__(self, cliente):
        super(VistaIngresso, self).__init__()

        self.cliente = cliente
        self.controller = ControlloreCliente(cliente)
        self.controllore_entrate = ControlloreListaEntrate()

        v_layout = QVBoxLayout()
        self.numero_ingressi = QListView()
        self.visualizzazione_ingresso()
        v_layout.addWidget(self.numero_ingressi)

        btn_aggiungi = QPushButton("Aggiungi Ingresso")
        btn_aggiungi.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        btn_aggiungi.setStyleSheet("border: 2px solid;" +
                                      "border-radius: 11px;" +
                                      "font-size: 22px;" +
                                   "font-weight: bold;" +
                                      "color: 'black'"
                                      )
        btn_aggiungi.clicked.connect(self.add_ingresso_click)
        v_layout.addWidget(btn_aggiungi)

        v_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_rimuovi = QPushButton("Rimuovi Ingresso")
        btn_rimuovi.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        btn_rimuovi.setStyleSheet("border: 2px solid;" +
                                      "border-radius: 11px;" +
                                      "font-size: 22px;" +
                                  "font-weight: bold;" +
                                      "color: 'black'"
                                      )
        btn_rimuovi.clicked.connect(self.rimuovi_ingresso_click)
        v_layout.addWidget(btn_rimuovi)

        self.setLayout(v_layout)
        self.resize(600, 300)
        self.setWindowTitle('Ingressi')

    def add_ingresso_click(self):
        self.controller.add_ingresso()
        self.visualizzazione_ingresso()
        self.controllore_entrate.aggiungi_entrata("Ingresso", 5)


    def rimuovi_ingresso_click(self):
        self.controller.rimuovi_ingresso()
        self.visualizzazione_ingresso()

    def visualizzazione_ingresso(self):
        self.numeroingressi_model = QStandardItemModel(self.numero_ingressi)
        tot = self.controller.get_ingressi_cliente()
        item = QStandardItem()
        totale = str(tot)
        item.setText("[Ingressi totali] " + totale)
        font = item.font()
        font.setPointSize(25)
        item.setFont(font)
        self.numeroingressi_model.appendRow(item)
        self.numero_ingressi.setModel(self.numeroingressi_model)

    def get_ingressi_cliente(self):
        return self.controller.get_ingressi_cliente()
