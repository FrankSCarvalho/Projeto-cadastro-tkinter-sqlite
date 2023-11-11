# Importando TkInter
from tkinter import *

from tkcalendar import Calendar, DateEntry

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


# dividindo janela

frame_cima = Frame(janela, width=310, height=50, bg=co2, relief='flat')
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=310, height=400, bg=co1, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

frame_esquerda = Frame(janela, width=588, height=400, bg=co1, relief='flat')
frame_esquerda.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)


#Label cima

app_nome = Label(frame_cima, text='Formulário de consultoria',  font=('Ivy 13 bold'), bg=co2, fg=co1, relief='flat')
app_nome.place(x=10, y=20)


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
b_inserir = Button(frame_baixo, text='Inserir', width=10, font=('Ivy 9 bold'), bg=co6, fg=co1, relief='raised', overrelief='ridge')
b_inserir.place(x=15, y=330)

#Botão Atualizar
b_atualizar = Button(frame_baixo, text='Atualizar', width=10, font=('Ivy 9 bold'), bg=co2, fg=co1, relief='raised', overrelief='ridge')
b_atualizar.place(x=110, y=330)

#Botão Excluir
b_excluir = Button(frame_baixo, text='Excluir', width=10, font=('Ivy 9 bold'), bg=co7, fg=co1, relief='raised', overrelief='ridge')
b_excluir.place(x=205, y=330)


janela.mainloop()
