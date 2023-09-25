from tkinter import *
from tkinter import ttk


cor1= "#121211"  # black/preto
cor2= "#f7f6f2"  # white/branco
cor3= "#162863"  # blue/azul
cor4= "#50535c"  # cinza
cor5= "#c95f12"  # laranja

janela = Tk()
janela.title("Calculadora Python")
janela.geometry("290x300")
janela.config(bg=cor1)


frame_tela = Frame(janela, width=290, height=60, bg=cor3) # tamanho do visor
frame_tela.grid(row=0, column=0)  #coluna e linha que o visor vai ficar

frame_corpo = Frame(janela, width=290, height=268, bg=cor1) # tamanho do visor
frame_corpo.grid(row=1, column=0) 

#variavel todos valores

todos_valores = ''

#criando label

valor_texto = StringVar()

#criando funcao
def entrar_valores(event):

    global todos_valores

    todos_valores = todos_valores + str(event)
    

    #pasando para tela
    valor_texto.set(todos_valores)



    #calcular

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(resultado)

    #limpar tela

def limpar_tela():
    global todos_valores
    todos_valores=""
    valor_texto.set("")






app_label = Label(frame_tela, textvariable=valor_texto, width=20, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=cor4, fg=cor2)
app_label.place(x=2,y=0)

b_1 = Button(frame_corpo,command=limpar_tela, text="C", width=20, height=2, bg=cor1, fg=cor5,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE )
b_1.place(x=0, y=0)

b_3 = Button(frame_corpo, command= lambda: entrar_valores('%'), text="%", width=8, height=2, bg=cor1, fg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE  )
b_3.place(x=152, y=0)
b_4 = Button(frame_corpo, command= lambda: entrar_valores('%'), text="/", width=8, height=2, bg=cor1, fg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE  )
b_4.place(x=221, y=0)

b_5 = Button(frame_corpo, command= lambda: entrar_valores('7'), text="7", width=8, height=2, bg=cor1, fg=cor2,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=0, y=45)
b_6 = Button(frame_corpo, command= lambda: entrar_valores('8'), text="8", width=8, height=2, bg=cor1, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE )
b_6.place(x=83, y=45)
b_7 = Button(frame_corpo, command= lambda: entrar_valores('9'), text="9", width=8, height=2, bg=cor1, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE )
b_7.place(x=152, y=45)
b_8 = Button(frame_corpo, command= lambda: entrar_valores('*'), text="x", width=8, height=2, bg=cor1, fg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE  )
b_8.place(x=221, y=45)

b_9 = Button(frame_corpo, command= lambda: entrar_valores('4'), text="4", width=8, height=2, bg=cor1, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=0, y=90)
b_10 = Button(frame_corpo, command= lambda: entrar_valores('5'), text="5", width=8, height=2, bg=cor1, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE )
b_10.place(x=83, y=90)
b_11 = Button(frame_corpo, command= lambda: entrar_valores('6'), text="6", width=8, height=2, bg=cor1, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE )
b_11.place(x=152, y=90)
b_12 = Button(frame_corpo, command= lambda: entrar_valores('-'), text="-", width=8, height=2, bg=cor1, fg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE  )
b_12.place(x=221, y=90)

b_13 = Button(frame_corpo, command= lambda: entrar_valores('1'), text="1", width=8, height=2, bg=cor1, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=0, y=135)
b_14 = Button(frame_corpo, command= lambda: entrar_valores('2'), text="2", width=8, height=2, bg=cor1, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE )
b_14.place(x=83, y=135)
b_15 = Button(frame_corpo, command= lambda: entrar_valores('3'), text="3", width=8, height=2, bg=cor1, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE )
b_15.place(x=152, y=135)
b_16 = Button(frame_corpo, command= lambda: entrar_valores('+'), text="+", width=8, height=2, bg=cor1, fg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE  )
b_16.place(x=221, y=135)

b_17 = Button(frame_corpo, command= lambda: entrar_valores('0'), text="0", width=8, height=2, bg=cor1, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE )
b_17.place(x=0, y=186)
b_18 = Button(frame_corpo, command= lambda: entrar_valores('.'), text=".", width=8, height=2, bg=cor1, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE )
b_18.place(x=83, y=186)
b_19 = Button(frame_corpo, command= lambda: entrar_valores(','), text=",", width=8, height=2, bg=cor1, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE )
b_19.place(x=152, y=186)
b_20 = Button(frame_corpo, command= calcular, text="=", width=8, height=2, bg=cor1, fg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE  )
b_20.place(x=221, y=186)

janela.mainloop()
 