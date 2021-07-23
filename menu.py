from tkinter import *
import Banco
#_______________________________________________________________________________________________________________________

#Funções para botões.
#def ImpDados():
    #print(f'Nome:       {txtCodProduto.get()}')
    #print(f'Quantidade: {txtQuantidade.get()}')
    #print(f'Fornecedor: {txtFornecedor.get()}')
    #print(f'Preço:      R${float(txtValorProduto.get()):.2f}')

#_______________________________________________________________________________________________________________________
#Funções gravar dados
def cadastrar():
    if txtNomeProd.get() != '':
        vnome = txtNomeProd.get()
        vquantidade = txtQuantidade.get()
        vfornecedor = txtFornecedor.get()
        vvalor = txtValorProd.get()
        vquery = "INSERT INTO tb_estoque (T_NOMEPRODUTO, T_QUANTIDADE, T_FORNECEDOR, T_VALORPRODUTO) VALUES ('"+vnome+"', '"+vquantidade+"', '"+vfornecedor+"', '"+vvalor+"')"
        Banco.dml(vquery)
        txtNomeProd.delete(0, END)
        txtQuantidade.delete(0, END)
        txtFornecedor.delete(0, END)
        txtValorProd.delete(0, END)
        txtNomeProd.focus()
        print("Produto cadastrado")
    else:
        print('ERRO')
#_______________________________________________________________________________________________________________________
#Designer do form
#Criando um elemento da classe tk
loja = Tk()
loja.title('Loja')
loja.geometry('800x500')

#Label código do produto
lblCodigoProd = Label(loja, text='Código do produto:')
lblCodigoProd.place(x=10, y=10)
#Text box que recebe o código do produto
#txtCodigoProd = Entry(loja)
#txtCodigoProd.place(x=120, y=10, width=300, height=20)

#Label nome do produto
lblNomeProd = Label(loja, text='Nome do produto:')
lblNomeProd.place(x=10, y=40)
#Text box que recebe o nome do produto
txtNomeProd = Entry(loja)
txtNomeProd.place(x=120, y=40, width=300, height=20)

#Label Nome do Quantidade
lblQuantidade = Label(loja, text='Quantidade:')
lblQuantidade.place(x=10, y=70)
#Text box que recebe a quantidade
txtQuantidade = Entry(loja)
txtQuantidade.place(x=120, y=70, width=300, height=20)

#Label Nome do Quantidade
lblFornecedor = Label(loja, text='Fornecedor:')
lblFornecedor.place(x=10, y=100)
#Text box que recebe o nome do fornecedor
txtFornecedor = Entry(loja)
txtFornecedor.place(x=120, y=100, width=300, height=20)

#Label preço do produto
lblValorProd = Label(loja, text='Preço do produto:')
lblValorProd.place(x=10, y=130)
#Text box que recebe o preço do produto
txtValorProd = Entry(loja)
txtValorProd.place(x=120, y=130, width=300, height=20)

#-----------------------------------------------------------------------------------------------------------------------
#def btnmouse(evento):
   # print(evento)
#loja.bind('<Button-1>', btnmouse)
#Faz a execução do programa, executa os eventos, desenha as ferramentas e etc.
Button(loja, text='Cadastrar', command=cadastrar).place(x=430, y=130, width=100, height=20)
loja.mainloop()