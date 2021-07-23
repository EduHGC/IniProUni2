from tkinter import *
import Banco
from tkinter import messagebox
from tkinter import ttk
#_______________________________________________________________________________________________________________________
#Funções dos botões
#Botão de cadastrar
def cadastrar():
    if txtNomeProd1.get() != '' and txtQuantidade1.get() != '' and txtFornecedor1.get() != '' and txtValorProd1.get() != "":
        vnome = txtNomeProd1.get()
        vquantidade = txtQuantidade1.get()
        vfornecedor = txtFornecedor1.get()
        vvalor = txtValorProd1.get()
        vquery = "INSERT INTO tb_estoque (T_NOMEPRODUTO, T_QUANTIDADE, T_FORNECEDOR, T_VALORPRODUTO) VALUES ('"+vnome+"', '"+vquantidade+"', '"+vfornecedor+"', '"+vvalor+"')"
        Banco.dml(vquery)
        txtNomeProd1.delete(0, END)
        txtQuantidade1.delete(0, END)
        txtFornecedor1.delete(0, END)
        txtValorProd1.delete(0, END)
        txtNomeProd1.focus()
        messagebox.showinfo(title="Cadastro", message="Produto cadastrado com sucesso!")
    else:
        txtNomeProd1.focus()
        messagebox.showerror(title="Cadastro", message="Algum campo está vazio!")


#_______________________________________________________________________________________________________________________
#Criando o form
estoque = Tk()
estoque.title('Estoque')
estoque.geometry('800x500')
abas = ttk.Notebook(estoque)
abas.place(x=0, y=0, width=800, height=500)
#_______________________________________________________________________________________________________________________
#Aba de cadastro
aba1 = Frame(abas)
abas.add(aba1, text="Cadastrar")

aba1titulo = Frame(aba1, borderwidth=1, relief="sunken")
aba1titulo.place(x=5, y=10, width=785, height=60)
lblCadastro = Label(aba1titulo, text='Cadastro do Produto', font=("Arial", 30))
lblCadastro.place(x=5, y=120, width=100, height=50)
lblCadastro.pack()


#Label nome do produto
lblNomeProd1 = Label(aba1, text='Nome do produto:')
lblNomeProd1.place(x=5, y=120)
#Text box que recebe o nome do produto
txtNomeProd1 = Entry(aba1)
txtNomeProd1.place(x=125, y=120, width=300, height=20)

#Label Nome do Quantidade
lblQuantidade1 = Label(aba1, text='Quantidade:')
lblQuantidade1.place(x=5, y=150)
#Text box que recebe a quantidade
txtQuantidade1 = Entry(aba1)
txtQuantidade1.place(x=125, y=150, width=300, height=20)

#Label Nome do Quantidade
lblFornecedor1 = Label(aba1, text='Fornecedor:')
lblFornecedor1.place(x=5, y=180)
#Text box que recebe o nome do fornecedor
txtFornecedor1 = Entry(aba1)
txtFornecedor1.place(x=125, y=180, width=300, height=20)

#Label preço do produto
lblValorProd1 = Label(aba1, text='Preço do produto:')
lblValorProd1.place(x=5, y=210)
#Text box que recebe o preço do produto
txtValorProd1 = Entry(aba1)
txtValorProd1.place(x=125, y=210, width=300, height=20)
#_______________________________________________________________________________________________________________________

aba2 = Frame(abas)
abas.add(aba2, text="Editar")
aba2titulo = Frame(aba2, borderwidth=1, relief="sunken")
aba2titulo.place(x=5, y=10, width=785, height=60)
lblEditar = Label(aba2titulo, text='Alteração de Cadastro', font=("Arial", 30))
lblEditar.place(x=5, y=120, width=100, height=50)
lblEditar.pack()

#_______________________________________________________________________________________________________________________
aba3 = Frame(abas)
abas.add(aba3, text="Pesquisar")

aba4 = Frame(abas)
abas.add(aba4, text="Exluir")


def btnmouse(evento):
    print(evento)
estoque.bind('<Button-1>', btnmouse)


Button(aba1, text='Cadastrar', command=cadastrar).place(x=430, y=210, width=100, height=20)
estoque.mainloop()