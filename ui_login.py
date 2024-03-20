from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName("Login")
        Login.resize(532, 506)
        Login.setStyleSheet("background-color: rgb(0, 80, 121);")
        self.label = QLabel(Login)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(190, 30, 151, 141))
        self.label.setStyleSheet("background-color:None;")
        self.label.setPixmap(QPixmap("icons/icon_title.png"))
        self.label.setScaledContents(True)
        self.frame = QFrame(Login)
        self.frame.setObjectName("frame")
        self.frame.setGeometry(QRect(80, 140, 381, 321))
        self.frame.setStyleSheet("background-color: rgba(0,0,0,0.2)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.txt_login = QLineEdit(self.frame)
        self.txt_login.setObjectName("txt_login")
        self.txt_login.setGeometry(QRect(60, 60, 251, 31))
        self.txt_login.setStyleSheet("color:#fff; font-size: 16px;")
        self.txt_login.setAlignment(Qt.AlignCenter)
        self.btn_login = QPushButton(self.frame)
        self.btn_login.setObjectName("btn_login")
        self.btn_login.setGeometry(QRect(100, 230, 181, 41))
        self.btn_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_login.setStyleSheet("QPushButton{color: rgb(255, 255, 255); border-radius: 10px; font-size: 16px; background-color:rgb(0, 0, 10);;}\n"
"\n"
"QPushButton:hover{background-color: #fff; color:black}\n"
"\n"
"")
        self.txt_password = QLineEdit(self.frame)
        self.txt_password.setObjectName("txt_password")
        self.txt_password.setGeometry(QRect(60, 140, 251, 31))
        self.txt_password.setStyleSheet("color:#fff; font-size: 16px;")
        self.txt_password.setEchoMode(QLineEdit.Password)
        self.txt_password.setAlignment(Qt.AlignCenter)
        QWidget.setTabOrder(self.txt_login, self.txt_password)
        QWidget.setTabOrder(self.txt_password, self.btn_login)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", "Form", None))
        self.label.setText("")
        self.txt_login.setText("")
        self.txt_login.setPlaceholderText(QCoreApplication.translate("Login", "User", None))
        self.btn_login.setText(QCoreApplication.translate("Login", "LOGIN", None))
        self.txt_password.setText("")
        self.txt_password.setPlaceholderText(QCoreApplication.translate("Login", "Password", None))
    # retranslateUi

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Login = QMainWindow()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())
