from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QListView, QHBoxLayout, QSpacerItem, QSizePolicy

from listaentrate.controller.ControlloreListaEntrate import ControlloreListaEntrate


class VistaListaEntrate(QWidget):
    def __init__(self, parent = None):
        super(VistaListaEntrate, self).__init__(parent)
        self.controller = ControlloreListaEntrate()

        h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.update_ui()
        h_layout.addWidget(self.list_view)

        h_layout.addItem(QSpacerItem(30, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.list_tot = QListView()
        self.totale()
        h_layout.addWidget(self.list_tot)

        self.setLayout(h_layout)
        self.resize(1000, 400)
        self.setWindowTitle('Lista Entrate')

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for entrata in self.controller.get_lista_delle_entrate():
            item = QStandardItem()
            prezzo = str(entrata.prezzo)
            item.setText(entrata.nome + " €" + prezzo)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
            self.list_view.setModel(self.listview_model)

    def totale(self):
        self.listtot_model = QStandardItemModel(self.list_tot)
        tot = 0
        for a in self.controller.get_lista_delle_entrate():
            tot = tot + a.prezzo
        item = QStandardItem()
        totale = str(tot)
        item.setText("TOTALE: €" + totale)
        item.setEditable(False)
        font = item.font()
        font.setPointSize(25)
        item.setFont(font)
        self.listtot_model.appendRow(item)
        self.list_tot.setModel(self.listtot_model)

    def closeEvent(self, event):
        self.controller.save_data()
