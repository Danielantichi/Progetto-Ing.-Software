import sys

from PyQt5.QtWidgets import QApplication

from homee.views.VistaHome import VistaHome
from login.views.VistaLogin import VistaLogin

if __name__ == '__main__':
    app = QApplication(sys.argv)
    #home = VistaHome()
    #home.show()
    login = VistaLogin()
    login.show()
    sys.exit(app.exec())
