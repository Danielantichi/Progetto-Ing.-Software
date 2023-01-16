from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QSpacerItem, QSizePolicy, QMessageBox
from login.controller.ControlloreLogin import ControlloreLogin
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
from PyQt5.QtGui import QCursor


class VistaLogin(QWidget):
    def __init__(self, parent=None):
        super(VistaLogin, self).__init__(parent)
        self.lista_dipendenti = []
        self.controller = ControlloreLogin()

        self.v_layout = QVBoxLayout()

        label_nome = QLabel("[LOGIN - PALESTRA]")
        label_nome.setAlignment(QtCore.Qt.AlignCenter)
        font_nome = label_nome.font()
        font_nome.setPointSize(20)
        label_nome.setStyleSheet("font-weight: bold; color: black")
        label_nome.setFont(font_nome)
        self.v_layout.addWidget(label_nome)

        self.v_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.qlines = {}
        self.add_info_text("id", "Id")
        self.add_info_text("password", "Password")

        self.v_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_login = QPushButton("Login")
        btn_login.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        btn_login.setStyleSheet("border: 2px solid;" +
                                "border-radius: 11px;" +
                                "font-size: 20px;" +
                                "font-weight: bold;" +
                                "color: 'black'"
                                )
        btn_login.clicked.connect(self.login_dipendente)
        self.v_layout.addWidget(btn_login)

        image = QPixmap("PalestraLogo.jpg")
        logo = QLabel()
        logo.setPixmap(image)
        logo.setAlignment(QtCore.Qt.AlignCenter)
        logo.setStyleSheet("margin-top: 50px;")
        self.v_layout.addWidget(logo)

        self.setLayout(self.v_layout)
        self.resize(500, 450)
        self.setWindowTitle("Login")

    def add_info_text(self, nome, label):
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qlines[nome] = current_text
        self.v_layout.addWidget(current_text)

    def login_dipendente(self):
        if self.controller.login_dipentente(self.qlines["id"].text(), self.qlines["password"].text()) is False:
            QMessageBox.critical(self, 'Id e Password errati', 'Per favore, riprova.',
                                 QMessageBox.Ok, QMessageBox.Ok)
