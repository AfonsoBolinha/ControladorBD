from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from CaixaGui import Ui_Venda
import pyodbc

import warnings
from os import system

#warnings.filterwarnings("ignore")
pyodbc.drivers()


ZurrapaFilial = pyodbc.connect('Driver={SQL Server};'
                               'Server=DESKTOP-7PL23QJ\SQLEXPRESS;'
                               'Database=ZurrapaFilial;')
filial = ZurrapaFilial.cursor()

def bdint(valor):
    return str(valor).replace("(", "").replace(")", "").replace(",", "").replace("'", "").replace("'", "").replace(" ","")


def bdstring(string):
    return str(string).replace("(", "").replace(")", "").replace(",", "").replace("'", "").replace("'", "")



class Ui_AplicacaoCaixa(object):
    def abreCaixa(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Venda()
        self.ui.setupUi(self.window)
        self.window.show()

    def selectAbrir(self):
        empCaixa = filial.execute("""SELECT IDEmp FROM EmpCaixa""")
        for caixas in empCaixa:
            if int(bdint(caixas)) == self.IDE.value():
                self.abreCaixa()
        #empBalcao = filial.execute("""SELECT IDEmp FROM EmpBalcao""")
        #for balcoes in empBalcao:
        #    if int(bdint(balcoes)) == IDE:
        #        abreBalcao()


    def setupUi(self, AplicacaoCaixa):
        AplicacaoCaixa.setObjectName("AplicacaoCaixa")
        AplicacaoCaixa.resize(206, 156)
        AplicacaoCaixa.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Portugal))
        self.centralwidget = QtWidgets.QWidget(AplicacaoCaixa)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")

        self.Label1 = QtWidgets.QLabel(self.centralwidget)
        self.Label1.setGeometry(QtCore.QRect(10, 20, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Label1.setFont(font)
        self.Label1.setAutoFillBackground(False)
        self.Label1.setScaledContents(False)
        self.Label1.setObjectName("Label1")
        self.Label2 = QtWidgets.QLabel(self.centralwidget)
        self.Label2.setGeometry(QtCore.QRect(10, 60, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Label2.setFont(font)
        self.Label2.setAutoFillBackground(False)
        self.Label2.setScaledContents(False)
        self.Label2.setObjectName("Label2")

        self.IDB = QtWidgets.QSpinBox(self.centralwidget)
        self.IDB.setGeometry(QtCore.QRect(150, 10, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.IDB.setFont(font)
        self.IDB.setObjectName("IDB")

        self.IDE = QtWidgets.QSpinBox(self.centralwidget)
        self.IDE.setGeometry(QtCore.QRect(150, 60, 51, 31))

        font = QtGui.QFont()
        font.setPointSize(10)

        self.IDE.setFont(font)
        self.IDE.setObjectName("IDE")


        self.butaoInfo = QtWidgets.QPushButton(self.centralwidget)
        self.butaoInfo.clicked.connect(self.selectAbrir)
        self.butaoInfo.setGeometry(QtCore.QRect(10, 100, 191, 28))
        font = QtGui.QFont()

        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.butaoInfo.setFont(font)
        self.butaoInfo.setObjectName("butaoInfo")
        AplicacaoCaixa.setCentralWidget(self.centralwidget)

        self.retranslateUi(AplicacaoCaixa)
        QtCore.QMetaObject.connectSlotsByName(AplicacaoCaixa)
        self.butaoInfo.clicked.connect(self.selectAbrir)

    def retranslateUi(self, AplicacaoCaixa):
        _translate = QtCore.QCoreApplication.translate
        AplicacaoCaixa.setWindowTitle(_translate("AplicacaoCaixa", "Aplicação Caixa"))
        self.Label1.setText(_translate("AplicacaoCaixa", "Insira o Seu IDB"))
        self.Label2.setText(_translate("AplicacaoCaixa", "Insira o Seu IDE"))
        self.butaoInfo.setText(_translate("AplicacaoCaixa", "Continuar"))









if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    AplicacaoCaixa = QtWidgets.QMainWindow()
    ui = Ui_AplicacaoCaixa()
    ui.setupUi(AplicacaoCaixa)
    AplicacaoCaixa.show()
    sys.exit(app.exec_())


