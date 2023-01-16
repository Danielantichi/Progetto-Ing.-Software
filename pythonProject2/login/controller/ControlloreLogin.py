from login.model.Login import Login


class ControlloreLogin():
    def __init__(self):
        super(ControlloreLogin, self).__init__()
        self.model = Login()

    def login_dipentente(self, id, password):
        return self.model.login_dipentente(id, password)


