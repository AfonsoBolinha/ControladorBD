from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import pyodbc
from datetime import date
import warnings
from os import system

#warnings.filterwarnings("ignore")
hoje=date.today()
dia=hoje.strftime("%Y-%m-%d")
pyodbc.drivers()
print(dia)



ZurrapaFilial = pyodbc.connect('Driver={SQL Server};'
                               'Server=DESKTOP-7PL23QJ\SQLEXPRESS;'
                               'Database=ZurrapaFilial;')
filial = ZurrapaFilial.cursor()

def bdint(valor):
    return str(valor).replace("(", "").replace(")", "").replace(",", "").replace(" ","")


def bdstring(string):
    return str(string).replace("(", "").replace(")", "").replace(",", "").replace("'", "").replace("'", "")



class Ui_Venda(object):
    idbs = 0
    idemp=0
    teste=""
    produtos = [0,0,0,0,0,0,0]
    qtd = [0,0,0,0,0,0,0]
    apagar=0
    aguasPedido=0
    cafePedido=0
    miniPedido=0
    mediaPedido=0
    shotsPedido=0
    nataPedido=0
    outrosPedido=0
    clicked=0
    def aguas(self, apagar):
        self.clicked += 1
        qtdAguas = filial.execute("""SELECT Quantidade FROM StockLocal WHERE IDProduto = 1 AND IDLocal={}""".format(self.idbs))
        for aguinha in qtdAguas:
            aguateste=float(bdint(aguinha))
        if self.aguasPedido <= aguateste and aguateste>0:
            self.aguasPedido += 1
            self.apagar += 0.5
            self.aPagar.setText("{}€".format(self.apagar))
            self.artigos.setText("\nAgua x {}".format(self.aguasPedido))
            self.qtd[0] = self.aguasPedido
            self.produtos[0] = 1
        else:
            self.agua.setText("Sem Stock")
    #PAra adicionar texto criar variavel que vai guardar as varias strings

    def cafes(self,apagar):
        self.clicked += 1
        qtdCafes = filial.execute(
            """SELECT Quantidade FROM StockLocal WHERE IDProduto = 2 AND IDLocal={}""".format(self.idbs))
        for cafezinho in qtdCafes:
            cafeteste = float(bdint(cafezinho))
        if self.cafePedido <= cafeteste and cafeteste > 0:
            self.cafePedido += 1
            self.apagar += 0.6
            self.aPagar.setText("{}€".format(self.apagar))
            self.artigos.setText("\nCafe x {}".format(self.cafePedido))
            self.qtd[1] = self.cafePedido
            self.produtos[1] = 2
        else:
            self.cafe.setText("Sem Stock")

    def minis(self, apagar):
        self.clicked += 1
        qtdMinis = filial.execute(
            """SELECT Quantidade FROM StockLocal WHERE IDProduto = 3 AND IDLocal={}""".format(self.idbs))
        for minizinha in qtdMinis:
            miniteste = float(bdint(minizinha))
        if self.miniPedido <= miniteste and miniteste > 0:
            self.miniPedido += 1
            self.apagar += 0.5
            self.aPagar.setText("{}€".format(self.apagar))
            self.artigos.setText("\nMini x {}".format(self.miniPedido))
            self.qtd[2] = self.miniPedido
            self.produtos[2] = 3
        else:
            self.mini.setText("Sem Stock")

    def medias(self, apagar):
        self.clicked += 1
        qtdMedias = filial.execute(
            """SELECT Quantidade FROM StockLocal WHERE IDProduto = 4 AND IDLocal={}""".format(self.idbs))
        for mediazinha in qtdMedias:
            mediateste = float(bdint(mediazinha))
        if self.miniPedido <= mediateste and mediateste > 0:
            self.mediaPedido += 1
            self.apagar += 1
            self.aPagar.setText("{}€".format(self.apagar))
            self.artigos.setText("\nMedia x {}".format(self.mediaPedido))
            self.qtd[3] = self.mediaPedido
            self.produtos[3] = 4
        else:
            self.media.setText("Sem Stock")

    def shot(self, apagar):
        self.clicked += 1
        qtdShots = filial.execute(
            """SELECT Quantidade FROM StockLocal WHERE IDProduto = 5 AND IDLocal={}""".format(self.idbs))
        for shotzinho in qtdShots:
            shotteste = float(bdint(shotzinho))
        if self.shotsPedido <= shotteste and shotteste > 0:
            self.shotsPedido += 1
            self.apagar += 1
            self.aPagar.setText("{}€".format(self.apagar))
            self.artigos.setText("\nShot x {}".format(self.shotsPedido))
            self.qtd[4] = self.shotsPedido
            self.produtos[4] = 5
        else:
            self.shots.setText("Sem Stock")

    def natas(self, apagar):
        self.clicked += 1
        qtdNatas = filial.execute(
            """SELECT Quantidade FROM StockLocal WHERE IDProduto = 6 AND IDLocal={}""".format(self.idbs))
        for natinha in qtdNatas:
            natateste = float(bdint(natinha))
        if self.nataPedido <= natateste and natateste > 0:
            self.nataPedido += 1
            self.apagar += 1
            self.aPagar.setText("{}€".format(self.apagar))
            self.artigos.setText("\nNata x {}".format(self.nataPedido))
            self.qtd[5] = self.nataPedido
            self.produtos[5] = 6
        else:
            self.nata.setText("Sem Stock")

    def outros(self, apagar):
        self.clicked += 1
        qtdOutros = filial.execute("""SELECT Quantidade FROM StockLocal WHERE IDProduto = {} AND IDLocal={}""".format(self.IDP.value(), self.idbs))
        for outrinho in qtdOutros:
            outroteste = int(bdint(outrinho))
        if self.quantidade.value() <= outroteste and outroteste > 0:
            self.outrosPedido = self.quantidade.value()
            custoOutros = filial.execute("""SELECT Preco_Venda FROM Produtos WHERE IDPRODUTO={}""".format(self.IDP.value()))
            for custo in custoOutros:
                custinho = float(bdint(custo))
            self.apagar += custinho
            self.aPagar.setText("{}€".format(self.apagar))
            nomeOutros = filial.execute("""SELECT Nome FROM Produtos WHERE IDPRODUTO = {}""".format(self.IDP.value()))
            for teste in nomeOutros:
                testezinho = bdstring(teste)
            self.artigos.setText("\n{} x {}".format(testezinho, self.outrosPedido))
            self.qtd[6] = self.outrosPedido
            self.produtos[6] = self.IDP.value()
        else:
            self.artigos.setText("Sem Stock")

    def processamento(self):
        idpedido=filial.execute("""SELECT TOP 1 IDPedido FROM Pedido ORDER BY IDPedido DESC""")
        for id in idpedido:
            top=int(bdint(id))
        tops=top+1
        filial.execute("""INSERT INTO Pedido (IDPedido, Estado, Dia, IDLocal, IDEmp)
VALUES ({}, 'Aberto', GETDATE(), {}, {});""".format(tops, self.idbs, self.idemp))
        filial.commit()
        teste=0
        for produt in self.produtos:
            print(self.produtos)
            print(self.qtd)
            if produt != 0:
                qtds=self.qtd[teste]
                filial.execute("""INSERT INTO LinhaPedido (IDPedido, IDProduto,Quantidade)
                                    VALUES ({},{},{});""".format(tops,produt,qtds))
                filial.commit()
                teste+=1


    def setupUi(self, Venda):
        Venda.setObjectName("Venda")
        Venda.resize(713, 515)
        Venda.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Portugal))
        self.artigos = QtWidgets.QLabel(Venda)
        self.artigos.setGeometry(QtCore.QRect(561, 126, 152, 281))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(21, 181, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(214, 214, 214))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(86, 86, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(115, 115, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(21, 181, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(21, 181, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(214, 214, 214))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(21, 181, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(214, 214, 214))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(86, 86, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(115, 115, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(21, 181, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(21, 181, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(214, 214, 214))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(86, 86, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(21, 181, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(214, 214, 214))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(86, 86, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(115, 115, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(86, 86, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(86, 86, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(21, 181, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(21, 181, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(173, 173, 173))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.artigos.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.artigos.setFont(font)
        self.artigos.setStyleSheet("background-color: rgb(21, 181, 255);")
        self.artigos.setFrameShape(QtWidgets.QFrame.Box)
        self.artigos.setLineWidth(2)
        self.artigos.setText("")
        self.artigos.setTextFormat(QtCore.Qt.RichText)
        self.artigos.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.artigos.setWordWrap(False)
        self.artigos.setIndent(1)
        self.artigos.setObjectName("artigos")
        self.cabecalho = QtWidgets.QLabel(Venda)
        self.cabecalho.setGeometry(QtCore.QRect(0, -5, 721, 131))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(54, 109, 163))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 233, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 233, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 233, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 109, 163))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 233, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 233, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 233, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 233, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 233, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 233, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.cabecalho.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("HoloLens MDL2 Assets")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.cabecalho.setFont(font)
        self.cabecalho.setStyleSheet("background-color: rgb(211, 233, 255);")
        self.cabecalho.setObjectName("cabecalho")
        self.aPagar = QtWidgets.QLabel(Venda)
        self.aPagar.setGeometry(QtCore.QRect(560, 390, 161, 151))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aPagar.sizePolicy().hasHeightForWidth())
        self.aPagar.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.aPagar.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aPagar.setFont(font)
        self.aPagar.setStyleSheet("background-color:rgb(0, 0, 0)")
        self.aPagar.setFrameShape(QtWidgets.QFrame.Box)
        self.aPagar.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.aPagar.setLineWidth(10)
        self.aPagar.setMidLineWidth(0)
        self.aPagar.setObjectName("aPagar")
        self.backgrounhd = QtWidgets.QLabel(Venda)
        self.backgrounhd.setGeometry(QtCore.QRect(-10, 126, 571, 421))
        self.backgrounhd.setStyleSheet("background-color: rgb(21, 181, 255);")
        self.backgrounhd.setText("")
        self.backgrounhd.setObjectName("backgrounhd")
        self.agua = QtWidgets.QPushButton(Venda)
        self.agua.setGeometry(QtCore.QRect(20, 200, 100, 61))
        self.agua.setObjectName("agua")
        self.mini = QtWidgets.QPushButton(Venda)
        self.mini.setGeometry(QtCore.QRect(20, 320, 100, 61))
        self.mini.setObjectName("mini")
        self.media = QtWidgets.QPushButton(Venda)
        self.media.setGeometry(QtCore.QRect(200, 320, 100, 61))
        self.media.setObjectName("media")
        self.cafe = QtWidgets.QPushButton(Venda)
        self.cafe.setGeometry(QtCore.QRect(200, 200, 100, 61))
        self.cafe.setObjectName("cafe")
        self.shots = QtWidgets.QPushButton(Venda)
        self.shots.setGeometry(QtCore.QRect(20, 440, 100, 61))
        self.shots.setObjectName("shots")
        self.nata = QtWidgets.QPushButton(Venda)
        self.nata.setGeometry(QtCore.QRect(200, 440, 100, 61))
        self.nata.setObjectName("nata")
        self.labelIDP = QtWidgets.QLabel(Venda)
        self.labelIDP.setGeometry(QtCore.QRect(334, 200, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelIDP.setFont(font)
        self.labelIDP.setObjectName("labelIDP")
        self.IDP = QtWidgets.QSpinBox(Venda)
        self.IDP.setGeometry(QtCore.QRect(450, 200, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.IDP.setFont(font)
        self.IDP.setObjectName("IDP")
        self.infromacao = QtWidgets.QLabel(Venda)
        self.infromacao.setGeometry(QtCore.QRect(10, 140, 551, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.infromacao.setFont(font)
        self.infromacao.setObjectName("infromacao")
        self.labelQuantidade = QtWidgets.QLabel(Venda)
        self.labelQuantidade.setGeometry(QtCore.QRect(334, 270, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelQuantidade.setFont(font)
        self.labelQuantidade.setObjectName("labelQuantidade")
        self.quantidade = QtWidgets.QSpinBox(Venda)
        self.quantidade.setGeometry(QtCore.QRect(450, 270, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.quantidade.setFont(font)
        self.quantidade.setObjectName("quantidade")
        self.processar = QtWidgets.QPushButton(Venda)
        self.processar.setGeometry(QtCore.QRect(330, 440, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.processar.setFont(font)
        self.processar.setObjectName("processar")
        self.adicionar = QtWidgets.QPushButton(Venda)
        self.adicionar.setGeometry(QtCore.QRect(330, 340, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.adicionar.setFont(font)
        self.adicionar.setObjectName("adicionar")
        self.remover = QtWidgets.QPushButton(Venda)
        self.remover.setGeometry(QtCore.QRect(330, 390, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.remover.setFont(font)
        self.remover.setObjectName("remover")
        self.aPagar.raise_()
        self.artigos.raise_()
        self.cabecalho.raise_()
        self.backgrounhd.raise_()
        self.agua.raise_()
        self.mini.raise_()
        self.media.raise_()
        self.cafe.raise_()
        self.shots.raise_()
        self.nata.raise_()
        self.labelIDP.raise_()
        self.IDP.raise_()
        self.infromacao.raise_()
        self.labelQuantidade.raise_()
        self.quantidade.raise_()
        self.processar.raise_()
        self.adicionar.raise_()
        self.remover.raise_()

        self.retranslateUi(Venda)
        QtCore.QMetaObject.connectSlotsByName(Venda)
        self.agua.clicked.connect(lambda: self.aguas(self.apagar))
        self.cafe.clicked.connect(lambda: self.cafes(self.aPagar))
        self.mini.clicked.connect(lambda: self.minis(self.aPagar))
        self.media.clicked.connect(lambda: self.medias(self.aPagar))
        self.shots.clicked.connect(lambda: self.shot(self.aPagar))
        self.nata.clicked.connect(lambda: self.natas(self.aPagar))
        self.adicionar.clicked.connect(lambda: self.outros(self.aPagar))
        self.IDP.setMaximum(7)
        self.IDP.setMinimum(1)
        self.processar.clicked.connect(lambda: self.processamento())

    def retranslateUi(self, Venda):
        _translate = QtCore.QCoreApplication.translate
        Venda.setWindowTitle(_translate("Venda", "Venda"))
        self.cabecalho.setText(_translate("Venda", "    Sistema de Venda Ao Cliente"))
        self.aPagar.setText(_translate("Venda", "0,00€"))
        self.agua.setText(_translate("Venda", "Agua"))
        self.mini.setText(_translate("Venda", "Mini"))
        self.media.setText(_translate("Venda", "Media"))
        self.cafe.setText(_translate("Venda", "Cafe"))
        self.shots.setText(_translate("Venda", "Shots"))
        self.nata.setText(_translate("Venda", "Nata"))
        self.labelIDP.setText(_translate("Venda", "Insira O IDP"))
        self.infromacao.setText(_translate("Venda", "Se o Produto Não Estiver nos butoes siga os paços ao lado dos mesmos:"))
        self.labelQuantidade.setText(_translate("Venda", "Quantidade"))
        self.processar.setText(_translate("Venda", "Processar"))
        self.adicionar.setText(_translate("Venda", "Adicionar"))
        self.remover.setText(_translate("Venda", "Remover"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Venda = QtWidgets.QWidget()
    ui = Ui_Venda()
    ui.setupUi(Venda)
    Venda.show()
    sys.exit(app.exec_())
