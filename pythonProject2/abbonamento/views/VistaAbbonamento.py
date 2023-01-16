from PyQt5 import QtCore
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QSpacerItem, QSizePolicy

from abbonamento.controller.ControlloreAbbonamento import ControlloreAbbonamento
from abbonamento.model.Abbonamento import Abbonamento
from abbonamento.views.VistaCongelaAbbonamento import VistaCongelaAbbonamento
from listaentrate.controller.ControlloreListaEntrate import ControlloreListaEntrate


class VistaAbbonamento(QWidget):
    def __init__(self, abbonamento, callback_inserici_abbonamento):
        super(VistaAbbonamento, self).__init__()
        self.controller = ControlloreAbbonamento(abbonamento)
        self.callback_inserisci_abbonamento = callback_inserici_abbonamento
        self.controllerentrate = ControlloreListaEntrate()
        self.abbonamento = abbonamento

        self.v_layout = QVBoxLayout()
        if self.controller.is_abbonato():
            label = QLabel(self.controller.get_scadenza_string())
            label.setAlignment(QtCore.Qt.AlignCenter)
            font_nome = label.font()
            font_nome.setPointSize(15)
            label.setFont(font_nome)
            self.v_layout.addWidget(label)

            self.v_layout.addItem(QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))

            btn_congela = QPushButton("Congela Abbonamento")
            btn_congela.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
            btn_congela.setStyleSheet("border: 2px solid;" +
                                  "border-radius: 11px;" +
                                  "font-size: 17px;" +
                                  "font-weight: bold;" +
                                  "color: 'black'"
                                  )
            btn_congela.clicked.connect(self.prolunga_abbonamento)
            self.v_layout.addWidget(btn_congela)
        else:
            label_1 = QLabel("Cliente non abbonato, scegli un abbonamento per favore")
            label_1.setAlignment(QtCore.Qt.AlignCenter)
            font_nome = label_1.font()
            font_nome.setPointSize(15)
            label_1.setFont(font_nome)
            self.v_layout.addWidget(label_1)

            btn_mensile = QPushButton("Aggiungi Abbonamento Mensile")
            btn_mensile.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
            btn_mensile.setStyleSheet("border: 2px solid;" +
                                          "border-radius: 11px;" +
                                          "font-size: 19px;" +
                                      "font-weight: bold;" +
                                          "color: 'black'"
                                          )
            btn_mensile.clicked.connect(self.abbonamento_mensile)
            self.v_layout.addWidget(btn_mensile)

            btn_trimestrale = QPushButton("Aggiungi Abbonamento Trimestrale")
            btn_trimestrale.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
            btn_trimestrale.setStyleSheet("border: 2px solid;" +
                                          "border-radius: 11px;" +
                                          "font-size: 19px;" +
                                          "font-weight: bold;" +
                                          "color: 'black'"
                                          )
            btn_trimestrale.clicked.connect(self.abbonamento_trimestrale)
            self.v_layout.addWidget(btn_trimestrale)

            btn_annuale = QPushButton("Aggiungi Abbonamento Annuale")
            btn_annuale.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
            btn_annuale.setStyleSheet("border: 2px solid;" +
                                          "border-radius: 11px;" +
                                          "font-size: 19px;" +
                                      "font-weight: bold;" +
                                          "color: 'black'"
                                          )
            btn_annuale.clicked.connect(self.abbonamento_annuale)
            self.v_layout.addWidget(btn_annuale)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Abbonamento")
        self.resize(300, 250)


    def abbonamento_mensile(self):
        self.controllerentrate.aggiungi_entrata("Abbonamento Mensile", 60)
        self.callback_inserisci_abbonamento(Abbonamento("MENSILE"))
        self.close()

    def abbonamento_trimestrale(self):
        self.controllerentrate.aggiungi_entrata("Abbonamento Trimestrale", 150)
        self.callback_inserisci_abbonamento(Abbonamento("TRIMESTRALE"))
        self.close()

    def abbonamento_annuale(self):
        self.controllerentrate.aggiungi_entrata("Abbonamento Annuale", 450)
        self.callback_inserisci_abbonamento(Abbonamento("ANNUALE"))
        self.close()

    def prolunga_abbonamento(self):
        self.congela_abbonamento = VistaCongelaAbbonamento(self.abbonamento)
        self.congela_abbonamento.show()
