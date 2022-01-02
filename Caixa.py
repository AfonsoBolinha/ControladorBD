import pyodbc
from datetime import date
import warnings
from os import system


today = date.today()
pyodbc.drivers()

ZurrapaSede = pyodbc.connect('Driver={SQL Server};'
                             'Server=DESKTOP-7PL23QJ\SQLEXPRESS;'
                             'Database=Ciclistas;')
sede = ZurrapaSede.cursor()

ZurrapaFilial = pyodbc.connect('Driver={SQL Server};'
                               'Server=DESKTOP-7PL23QJ\SQLEXPRESS;'
                               'Database=ZurrapaFilial;')
filial = ZurrapaFilial.cursor()
warnings.filterwarnings("ignore")


def bdstring(string):
    return str(string).replace("(", "").replace(")", "").replace(",", "").replace("'", "").replace("'", "")


def bdint(valor):
    teste= str(valor).replace("(", "").replace(")", "").replace(",", "").replace("'", "").replace("'", "").replace(" ",
                                                                                                                "")
    return teste


def menusimples():
    print("1- Adicionar Pedido\n2- Fechar Pedido\n3- Verificar Pedidos Abertos\n")


def produtos():
    produto = filial.execute("""SELECT * FROM Produtos""")
    for produtos in produto:
        print(bdstring(produtos), end="")
        print("€")

def aberturapedido(IDB):
    IDpedido = filial.execute("""SELECT TOP 1 IDpedido
                                        FROM Caixas
                                        WHERE IDB={}
                                         ORDER BY IDpedido DESC""".format(IDB))
    for pedidos in IDpedido:
        ID = int(bdint(pedidos))
    pedido = ID + 1
    filial.execute("""INSERT INTO Caixas (IDpedido, Estado, IDB)
                          VALUES ({}, 'Aberto', {});""".format(pedido, IDB))
    filial.commit()

def fechapedidos(IDB):
    estados = filial.execute("""SELECT IDpedido 
                                    FROM Caixas 
                                     WHERE Estado LIKE 'Abe%' AND IDB = {} 
                                     ORDER BY IDestado ASC""".format(IDB))
    for estado in estados:
        print(int(bdint(estado)))
    fechaPedido = int(input("Qual pedido pretende fechar? "))
    filial.execute("""UPDATE Caixas
                          SET Estado = 'Fechado'
                            WHERE IDpedido= {} AND IDB={};""".format(fechaPedido, IDB))
    filial.commit()


def venda(quantidade, opcaoprodutoqtd, IDB, opcaoproduto):
    filial.execute("""UPDATE Armazem_Bar
                                   SET QTD = {}
                                   WHERE IDB={} AND IDP={};""".format((int(bdint(quantidade)) - opcaoprodutoqtd), IDB,
                                                                      opcaoproduto))
    gastos = filial.execute("""SELECT CustoOrigem FROM Armazem_Bar WHERE IDP = {};""".format(opcaoproduto))
    lucros = filial.execute("""SELECT CustoRevenda FROM Armazem_Bar WHERE IDP = {};""".format(opcaoproduto))
    filial.execute("""INSERT INTO Financas (Data,Gastos,Lucros)
                                   VALUES ({}, {}, {});""".format(today.strftime("%Y/%m/%d"),
                                                                  (int(bdint(gastos)) * opcaoprodutoqtd),
                                                                  (int(bdint(lucros)) * opcaoprodutoqtd)))
    filial.execute("""INSERT INTO Venda (Data,IDPunitario,Quantidade_Vendido)
                                   VALUES ({}, {}, {});""".format(today.strftime("%Y/%m/%d"), opcaoproduto,
                                                                  opcaoproduto))
    filial.commit()


def caixapedido(IDB):
    print("1- Adicionar produto ao pedido\n2- Processar Pedido")
    opcaopedido = int(input("Escolha a opcao: "))
    while (opcaopedido != 1) and (opcaopedido != 2):
        print("1- Adicionar produto ao pedido\n2-Processar Pedido")
        opcaopedido = int(input("Escolha a opcao: "))
    if opcaopedido == 1:
        produtos()
        opcaoproduto = int(input("Escolha o IDB do produto que pretende: "))
        opcaoprodutoqtd = int(input("Qual a quantidade: "))
        quantidade = filial.execute(
            """SELECT QTD FROM Armazem_Bar WHERE IDP = {} AND IDB = {} """.format(opcaoproduto, IDB))
        if int(bdint(quantidade)) >= opcaoprodutoqtd:
            venda(int(bdint(quantidade)), opcaoprodutoqtd, IDB, opcaoproduto)
        if int(bdint(quantidade)) < opcaoprodutoqtd:
            quantidadeArmazem = filial.execute(
                """SELECT QTD FROM Armazem_Filial WHERE IDPpack = {}""".format(opcaoproduto))
            quantidadePack = filial.execute("""SELECT QtdPack FROM Valor_Conversao WHERE IDP= {}""".format(opcaoproduto))
            if opcaoprodutoqtd <= int(bdint(quantidadeArmazem)) * int(bdint(quantidadePack)):
                pedidoPacks = round(opcaoprodutoqtd / int(bdint(quantidadePack)))
                filial.execute("""UPDATE Armazem_Filial SET QTD={} WHERE IDPpack={}""".format((int(bdint(quantidadeArmazem))-pedidoPacks),opcaoproduto))
                filial.execute("""UPDATE Armazem_Bar SET QTD={} WHERE IDP={} AND IDB={}""".format((int(bdint(quantidade))+(pedidoPacks*int(bdint(quantidadePack)))),opcaoproduto,IDB))
                venda(int(bdint(quantidade)), opcaoprodutoqtd, IDB, opcaoproduto)
            if opcaoprodutoqtd>int(bdint(quantidadeArmazem)) * int(bdint(quantidadePack)):
                fechapedidos(IDB)



            
# Inicio do programa
#produtos()
IDB = int(input("Qual o seu IDB? "))

# Seleção de Ação
menusimples()
caixa = int(input("Escolha uma opção: "))
while (caixa != 1) and (caixa != 2) and (caixa != 3) and (caixa != 4):
    system("cls")
    print("\n")
    menusimples()
    caixa = int(input("Escolha Opção: "))

# Adicionar um pedido
if caixa == 1:
    caixapedido(IDB)
if caixa == 2:
    fechapedidos(IDB)

if caixa == 3:
    caixa3 = filial.execute("""SELECT IDpedido, Estado 
                                FROM CAIXAS 
                                WHERE Estado LIKE 'Abe%' AND IDB={} 
                                ORDER BY IDpedido ASC;""".format(IDB))
    for i in caixa3:
        print(bdstring(i))
