# Importando TkInter
from tkinter import *

from tkinter import ttk
from tkinter import messagebox

# importando o Calendario para Data
from tkcalendar import Calendar, DateEntry

from view import *

################# cores ###############
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # sky blue

# Criando Janela

janela = Tk()

janela.title("")
janela.geometry("1043x453")
janela.configure(background=co9)

janela.resizable(width=FALSE, height=FALSE)


# dividindo janela em 3 frames

frame_cima = Frame(janela, width=310, height=50, bg=co2, relief='flat')
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=310, height=400, bg=co1, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

frame_direita = Frame(janela, width=588, height=400, bg=co1, relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)


#Label de Titulo no Frame de cima
app_nome = Label(frame_cima, text='Formulário de consultoria',  font=('Ivy 13 bold'), bg=co2, fg=co1, relief='flat')
app_nome.place(x=10, y=20)

global tree


#Função inserir
def inserir():
    nome = e_nome.get()
    email = e_email.get()
    telefone = e_telefone.get()
    data = e_data.get()
    estado = e_estado.get()
    sobre = e_sobre.get()

    lista = [nome, email,telefone,data,estado,sobre]

    if nome == "":
        messagebox.showerror('Erro', 'Preencha o campo nome')
    else:
        inserir_info(lista)
        messagebox.showinfo('Sucesso', 'Dados gravados com sucesso!')

        e_nome.delete(0,'end')
        e_email.delete(0,'end')
        e_telefone.delete(0,'end')
        e_data.delete(0,'end')
        e_estado.delete(0,'end')
        e_sobre.delete(0,'end')


    for widget in frame_direita.winfo_children():
        widget.destroy()

    mostrar()

#Função Atualizar
def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        valor_id = tree_lista[0]

        e_nome.delete(0,'end')
        e_email.delete(0,'end')
        e_telefone.delete(0,'end')
        e_data.delete(0,'end')
        e_estado.delete(0,'end')
        e_sobre.delete(0,'end')

        e_nome.insert(0, tree_lista[1])
        e_email.insert(0, tree_lista[2])
        e_telefone.insert(0, tree_lista[3])
        e_data.insert(0, tree_lista[4])
        e_estado.insert(0, tree_lista[5])
        e_sobre.insert(0, tree_lista[6])

        #Função inserir
        def update():
            nome = e_nome.get()
            email = e_email.get()
            telefone = e_telefone.get()
            data = e_data.get()
            estado = e_estado.get()
            sobre = e_sobre.get()

            lista = [ nome, email,telefone,data,estado,sobre,valor_id]

            if nome == "":
                messagebox.showerror('Erro', 'Preencha o campo nome')
            else:
                atualizar_info(lista)
                messagebox.showinfo('Sucesso', 'Dados atualizados com sucesso!')

                e_nome.delete(0,'end')
                e_email.delete(0,'end')
                e_telefone.delete(0,'end')
                e_data.delete(0,'end')
                e_estado.delete(0,'end')
                e_sobre.delete(0,'end')


            for widget in frame_direita.winfo_children():
                widget.destroy()

            mostrar()

        #Botão Confirmar
        b_confirmar = Button(frame_baixo, command=update, text='Confirmar', width=10, font=('Ivy 9 bold'), bg=co2, fg=co1, relief='raised', overrelief='ridge')
        b_confirmar.place(x=110, y=360)

        
    except IndexError:
        messagebox.showerror('Erro', 'Selecione um dos dados na tabela')

#função deletar
def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        valor_id = [tree_lista[0]]

        deletar_info(valor_id)
        messagebox.showinfo('Sucesso', 'Dados deletados com sucesso!')

        for widget in frame_direita.winfo_children():
                widget.destroy()

        mostrar()

    except IndexError:
        messagebox.showerror('Erro', 'Selecione um dos dados na tabela')


#Configurando Frame Baixo
#Nome
l_nome = Label(frame_baixo, text='Nome: *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_nome.place(x=10, y=10)
e_nome = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_nome.place(x=15, y=40)

#Email
l_email = Label(frame_baixo, text='Email: ', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_email.place(x=10, y=70)
e_email = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_email.place(x=15, y=100)


#Telefone
l_telefone = Label(frame_baixo, text='Telefone: ', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_telefone.place(x=10, y=130)
e_telefone = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_telefone.place(x=15, y=160)

#Data
l_data = Label(frame_baixo, text='Data da Consulta: ', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_data.place(x=10, y=190)
e_data = DateEntry(frame_baixo, width=15, backgroung='darkblue', foreground='white', borderwidth=2)
e_data.place(x=15, y=220)


#Estado
l_estado = Label(frame_baixo, text='Estado da Consulta: ', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_estado.place(x=160, y=190)
e_estado = Entry(frame_baixo, width=20, justify='left', relief='solid')
e_estado.place(x=165, y=220)

#Sobre
l_sobre = Label(frame_baixo, text='Informações extras: ', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_sobre.place(x=10, y=250)
e_sobre = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_sobre.place(x=15, y=280)

#Botões

#Botão Inserir
b_inserir = Button(frame_baixo, command=inserir, text='Inserir', width=10, font=('Ivy 9 bold'), bg=co6, fg=co1, relief='raised', overrelief='ridge')
b_inserir.place(x=15, y=330)

#Botão Atualizar
b_atualizar = Button(frame_baixo,command=atualizar, text='Atualizar', width=10, font=('Ivy 9 bold'), bg=co2, fg=co1, relief='raised', overrelief='ridge')
b_atualizar.place(x=110, y=330)

#Botão Excluir
b_excluir = Button(frame_baixo, command=deletar, text='Excluir', width=10, font=('Ivy 9 bold'), bg=co7, fg=co1, relief='raised', overrelief='ridge')
b_excluir.place(x=205, y=330)



def mostrar():

    global tree

    lista = mostrar_info()

    # lista para cabecario
    tabela_head = ['ID','Nome',  'email','telefone', 'Data', 'Estado','Sobre']


    # criando a tabela
    tree = ttk.Treeview(frame_direita, selectmode="extended", columns=tabela_head, show="headings")

    # vertical scrollbar
    vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar( frame_direita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    frame_direita.grid_rowconfigure(0, weight=12)


    hd=["nw","nw","nw","nw","nw","center","center"]
    h=[30,170,140,100,120,50,100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in lista:
        tree.insert('', 'end', values=item)


mostrar()

janela.mainloop()
