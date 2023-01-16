from PyQt5.QtGui import QStandardItemModel, QStandardItem, QCursor, QFont
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton, QSpacerItem, QSizePolicy
from PyQt5 import QtCore

from attivita.views.VistaAttivita import VistaAttivita
from listaattivita.controller.ControlloreListaAttivita import ControlloreListaAttivita


class VistaListaAttivita(QWidget):
    def __init__(self, parent=None):
        super(VistaListaAttivita, self).__init__(parent)
        self.controller = ControlloreListaAttivita()

        h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.listview_model = QStandardItemModel(self.list_view)
        for attivita in self.controller.get_lista_delle_attivita():
            item = QStandardItem()
            item.setText(attivita.nome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)
        h_layout.addWidget(self.list_view)

        h_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        buttons_layout = QVBoxLayout()
        open_button = QPushButton("Apri")
        open_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        open_button.setStyleSheet("border: 2px solid;" +
                                  "border-radius: 11px;" +
                                  "font-size: 22px;" +
                                  "font-weight: bold;" +
                                  "color: 'black'"
                                  )
        open_button.clicked.connect(self.show_selected_info)
        buttons_layout.addWidget(open_button)
        buttons_layout.addStretch()
        h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        self.resize(600, 300)
        self.setWindowTitle('Lista Attivita')

    def show_selected_info(self):
        if (len(self.list_view.selectedIndexes()) > 0):
            selected = self.list_view.selectedIndexes()[0].row()
            attivita_selezionata = self.controller.get_attivita_by_index(selected)
            self.vista_attivita = VistaAttivita(attivita_selezionata)
            self.vista_attivita.show()

    def closeEvent(self, event):
        print("ON CLOSE")
        self.controller.save_data()
        event.accept()
