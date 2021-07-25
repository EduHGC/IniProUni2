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

    #Botão pesquisar por código
def pesquisaCod():
    if txtCodigoProdPes.get() != '':
        try:
            tvPesquisa.delete(*tvPesquisa.get_children())
            vcodigo = txtCodigoProdPes.get()
            vpesquisa = "SELECT * FROM tb_estoque WHERE T_CODIGOPRODUTO="+vcodigo
            resultadoPes = Banco.dql(vpesquisa)
            #Resultado para gerar erro de código não existente
            resCodigo = resultadoPes[0][0]
            for i in resultadoPes:
                tvPesquisa.insert('', 'end', values=i)
            txtCodigoProdPes.delete(0, END)

        except:
            messagebox.showerror(title="Erro", message="Código não Cadastrado")
            txtCodigoProdPes.delete(0, END)

    elif txtNomeProdPes.get() != '':
        try:
            tvPesquisa.delete(*tvPesquisa.get_children())
            vnome = txtNomeProdPes.get()
            vpesquisanome = "SELECT * FROM tb_estoque WHERE T_NOMEPRODUTO LIKE '%"+vnome+"%'"
            resultadoPes = Banco.dql(vpesquisanome)
            resnome = resultadoPes[0][1]
            for i in resultadoPes:
                tvPesquisa.insert('', 'end', values=i)
            txtNomeProdPes.delete(0, END)

        except:
            messagebox.showerror(title="Erro", message="Produto não castrado!")
            txtNomeProdPes.delete(0, END)
    else:
        messagebox.showerror(title="Erro", message="Campo para pesquisa vazio!")

def listarTodos():
    tvPesquisa.delete(*tvPesquisa.get_children())
    vlistar = "SELECT * FROM tb_estoque order by T_CODIGOPRODUTO"
    listar = Banco.dql(vlistar)
    for i in listar:
        tvPesquisa.insert('', 'end', values=i)

#_______________________________________________________________________________________________________________________
#Criando o form
estoque = Tk()
estoque.title('Estoque')
estoque.geometry('800x600')
abas = ttk.Notebook(estoque)
abas.place(x=0, y=0, width=800, height=600)
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
#Aba de alteração
aba2 = Frame(abas)
abas.add(aba2, text="Editar")
aba2titulo = Frame(aba2, borderwidth=1, relief="sunken")
aba2titulo.place(x=5, y=10, width=785, height=60)
lblEditar = Label(aba2titulo, text='Alteração de Cadastro', font=("Arial", 30))
lblEditar.place(x=5, y=120, width=100, height=50)
lblEditar.pack()

#Label código do produto
lblCodigoProd = Label(aba2, text='Código do produto:')
lblCodigoProd.place(x=5, y=90)
#Text box que recebe o código do produto
txtCodigoProd = Entry(aba2)
txtCodigoProd.place(x=125, y=90, width=50, height=20)

#_______________________________________________________________________________________________________________________
#Aba pesquisar
aba3 = Frame(abas)
abas.add(aba3, text="Pesquisar")
aba3titulo = Frame(aba3, borderwidth=1, relief="sunken")
aba3titulo.place(x=5, y=10, width=785, height=60)
lblPesquisar = Label(aba3titulo, text='Pesquisar Produto', font=("Arial", 30))
lblPesquisar.place(x=5, y=120, width=100, height=50)
lblPesquisar.pack()

#Frame para pesquisa por código
lblfrPesquisaCod = LabelFrame(aba3, text='Pesquisar por Código: ')
lblfrPesquisaCod.place(x=5, y=90, width=250, height=60)

#Text box que receve o código do produto para pesquisar
lblCodigoProdPes = Label(lblfrPesquisaCod, text='Código do produto:')
lblCodigoProdPes.place(x=5, y=10)
#Text box que recebe o código do produto
txtCodigoProdPes = Entry(lblfrPesquisaCod)
txtCodigoProdPes.place(x=125, y=10, width=50, height=20)


#Frame para pesquisa por nome
lblfrPesquisaNome = LabelFrame(aba3, text='Pesquisar por Nome: ')
lblfrPesquisaNome.place(x=300, y=90, width=400, height=60)

#Label nome do nome
lblNomeProdPes = Label(lblfrPesquisaNome, text='Nome do produto:')
lblNomeProdPes.place(x=5, y=10)
#Text box que recebe o nome do produto para pesquisa
txtNomeProdPes = Entry(lblfrPesquisaNome)
txtNomeProdPes.place(x=125, y=10, width=250, height=20)

#TreeView para listar o resultado da pesquisa
tvPesquisa = ttk.Treeview(aba3, columns=('codigo', 'nome', 'quantidade', 'fornecedor', 'valor'), show='headings')
tvPesquisa.column('codigo', minwidth=0, width=130)
tvPesquisa.column('nome', minwidth=0, width=130)
tvPesquisa.column('quantidade', minwidth=0, width=130)
tvPesquisa.column('fornecedor', minwidth=0, width=130)
tvPesquisa.column('valor', minwidth=0, width=130)
tvPesquisa.heading('codigo', text='Código do produto')
tvPesquisa.heading('nome', text='Nome do produto')
tvPesquisa.heading('quantidade', text='Quantidade')
tvPesquisa.heading('fornecedor', text='Nome do Fornecedor')
tvPesquisa.heading('valor', text='Preço do Produto')
tvPesquisa.place(x=5, y=180, width=695, height=300)


#_______________________________________________________________________________________________________________________
aba4 = Frame(abas)
abas.add(aba4, text='Exluir')


def btnmouse(evento):
    print(evento)
estoque.bind('<Button-1>', btnmouse)


Button(aba1, text='Cadastrar', command=cadastrar).place(x=430, y=210, width=100, height=20)
Button(aba3, text='Pesquisar', command=pesquisaCod).place(x=490, y=485, width=100, height=20)
Button(aba3, text='Lista Todos', command=listarTodos).place(x=600, y=485, width=100, height=20)
estoque.mainloop()