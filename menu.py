from tkinter import *
#_______________________________________________________________________________________________________________________

#Funções para botões.
def ImpDados():
    print(f'Nome:       {txtCodProduto.get()}')
    print(f'Quantidade: {txtQuantidade.get()}')
    print(f'Fornecedor: {txtFornecedor.get()}')
    print(f'Preço:      R${float(txtValorProduto.get()):.2f}')

#_______________________________________________________________________________________________________________________

#Designer do form
#Criando um elemento da classe tk
loja = Tk()
loja.title('Loja')
loja.geometry('800x500')

#Label código do produto
lblCodPro = Label(loja, text='Código do produto:')
lblCodPro.place(x=10, y=10)
#Text box que recebe o código do produto
txtCodProduto = Entry(loja)
txtCodProduto.place(x=120, y=10, width=300, height=20)

#Label Nome do Quantidade
lblQuantidade = Label(loja, text='Quantidade:')
lblQuantidade.place(x=10, y=40)
#Text box que recebe a quantidade
txtQuantidade = Entry(loja)
txtQuantidade.place(x=120, y=40, width=300, height=20)

#Label Nome do Quantidade
lblFornecedor = Label(loja, text='Fornecedor:')
lblFornecedor.place(x=10, y=70)
#Text box que recebe o nome do fornecedor
txtFornecedor = Entry(loja)
txtFornecedor.place(x=120, y=70, width=300, height=20)

#Label preço do produto
lblValorProduto = Label(loja, text='Preço do produto:')
lblValorProduto.place(x=10, y=100)
#Text box que recebe o preço do produto
txtValorProduto = Entry(loja)
txtValorProduto.place(x=120, y=100, width=300, height=20)

#-----------------------------------------------------------------------------------------------------------------------
#def btnmouse(evento):
   # print(evento)
#loja.bind('<Button-1>', btnmouse)
#Faz a execução do programa, executa os eventos, desenha as ferramentas e etc.
Button(loja, text='Salvar', command=ImpDados).place(x=430, y=100, width=100, height=20)
loja.mainloop()