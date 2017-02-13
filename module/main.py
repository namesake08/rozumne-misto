import sys
from PyQt5.QtWidgets import *


class Settings(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Подписи для полей
        Login = QLabel('Login')
        Password = QLabel('Password')
        # Поля
        LoginEditField = QLineEdit()
        PasswordEditField = QLineEdit()
        LogInButton = QPushButton('Log in', self)
        LogInButton.move(200, 250)
        grid = QGridLayout()
        grid.setSpacing(1)

        grid.addWidget(Login, 1, 0)
        grid.addWidget(LoginEditField, 1, 1)

        grid.addWidget(Password, 2, 0)
        grid.addWidget(PasswordEditField, 2, 1)

        self.setLayout(grid)

        self.setGeometry(350, 350, 350, 350)
        self.setWindowTitle('Settings')
        self.show()



class StandartSetting(QWidget):
    def __init__(self, parent=None):
        super.__init__()
        self.InitUI(self)

    def InitUI(self):
        Login = QLabel('Login')
        self.LoginInp = QLabel(self)
        Password = QLabel('Password')
        self.PasswordInp = QLabel(self)
        LogOutButton = QPushButton('Log out', self)
        #LogOutButton.click(self.logOutButton)
        LogOutButton.move(200, 250)

    def loginbutton(self, login, password):
        self.LoginInp.setText(login)
        self.LoginInp.adjustSize()
        self.PasswordInp.setText(password)
        self.PasswordInp.adjustSize()

    def logOutButton(self):
        pass


def run():
    app = QApplication(sys.argv)
    ex = Settings()
    sys.exit(app.exec_())
