from datetime import datetime, time

from PyQt5 import QtCore
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox


class VistaCongelaAbbonamento(QWidget):
    def __init__(self, abbonamento):
        super(VistaCongelaAbbonamento, self).__init__()
        self.abbonamento = abbonamento

        v_layout = QVBoxLayout()

        label = QLabel("Aggiungi una nuova data di scadenza abbonamento (dd/MM/yyyy)")
        label.setAlignment(QtCore.Qt.AlignCenter)
        font_nome = label.font()
        font_nome.setPointSize(15)
        label.setFont(font_nome)
        v_layout.addWidget(label)

        self.text_scadenza = QLineEdit()
        v_layout.addWidget(self.text_scadenza)

        btn_prolunga = QPushButton("Prolunga Data")
        btn_prolunga.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        btn_prolunga.setStyleSheet("border: 2px solid;" +
                                  "border-radius: 11px;" +
                                  "font-size: 22px;" +
                                   "font-weight: bold;" +
                                  "color: 'black'"
                                  )
        btn_prolunga.clicked.connect(self.update_abbonamento_click)
        v_layout.addWidget(btn_prolunga)

        self.setLayout(v_layout)
        self.setWindowTitle("Congela Abbonamento")
        self.resize(300, 300)

    def update_abbonamento_click(self):
        try:
            date = datetime.strptime(self.text_scadenza.text(), '%d/%m/%Y')
            if date > self.abbonamento.scadenza:
                self.abbonamento.scadenza = date
                self.close()
            else:
                QMessageBox.critical(self, 'Errore', 'Inserisci una data maggiore di quella già esistente', QMessageBox.Ok, QMessageBox.Ok)
        except:
            QMessageBox.critical(self, 'Errore', 'Inserisci la data nel formato richiesto: dd/MM/yyyy', QMessageBox.Ok,
                                 QMessageBox.Ok)


