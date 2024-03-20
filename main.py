from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget, QTreeWidgetItem, QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from xml_files import Read_xml
from database import DataBase
import sys
import sqlite3
import pandas as pd
import re
from datetime import date
import matplotlib.pyplot as plt

from ui_login import Ui_Login
from ui_main import Ui_MainWindow

class Login(QWidget, Ui_Login):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.tentativas = 0
        self.setupUi(self)
        self.setWindowTitle("Gerenciamento de Sistema")
        appIcon = QIcon('_imagens/logotipo.PNG')
        self.setWindowIcon(appIcon)

        self.btn_login.clicked.connect(self.checkLogin)

    def checkLogin(self):
        self.users = DataBase()
        self.users.conecta()
        autenticado = self.users.check_user(self.txt_login.text().upper(), self.txt_password.text())

        if autenticado.lower() == "administrador" or autenticado.lower() == "user":
            self.w = MainWindow(self.txt_login.text(), autenticado.lower())
            self.w.show()
            self.close()
        else:
            if self.tentativas < 3:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Erro ao acessar")
                msg.setText(f'Login ou senha incorreto \n \n Tentativa: {self.tentativas +1} de 3')
                msg.exec_()
                self.tentativas += 1
            if self.tentativas == 3:
                # bloquear o usuário
                self.users.close_connection()
                sys.exit(0)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, username, user):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sistema de gerenciamento")
        appIcon = QIcon('_imgs/logo.PNG')
        self.setWindowIcon(appIcon)

        self.user = username
        if user.lower() == "user":
            self.btn_pg_cadastro.setVisible(False)

        # *************PAGINAS DO SISTEMA***********************************************
        self.btn_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))
        self.btn_tables.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_table))
        self.btn_contato.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_contato))
        self.btn_sobre.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_sobre))
        self.btn_pg_cadastro.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cadastro))
        self.btn_pg_import.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_import))

        self.btn_cadastrar.clicked.connect(self.subscribe_user)

        # ARQUIVO XML
        self.btn_open.clicked.connect(self.open_path)
        self.btn_import.clicked.connect(self.import_xml_files)

        # filtro
        self.txt_search.textChanged.connect(self.update_filter)

        # gerar saida e estorno
        self.btn_gerar.clicked.connect(self.gerar_saida)
        self.btn_estorno.clicked.connect(self.gerar_estorno)

        self.btn_excel.clicked.connect(self.excel_file)

        self.btn_chart.clicked.connect(self.graphic)

        self.reset_table()

    # Métodos de classe aqui

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    sys.exit(app.exec_())
