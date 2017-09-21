#*************************************************************************************************
#                                            EVENTOS
#*************************************************************************************************
#OBS:
#Muitos mais eventos estão disponíveis em: http://www.python-course.eu/tkinter_events_binds.php
#*************************************************************************************************
#INCLUDES
from tkinter import*
from tkinter.ttk import*
from main_code import *
#*************************************************************************************************
#CONSTANTES E DEFINIÇÕES
resolucao = '600x200+200+200'

#*************************************************************************************************
#EVENTOS
def apertou_tecla(event):                           #Função do evento de apertar a tecla
    trata_tecla(event.char, event.keycode)

def botao_direito(event):                           #O parâmetro event deve ser passado obrigatoriamente
    lb2['text']= trata_direito()

def on_leave(event):
    trata_mouse_out()

def on_enter(enter):
    trata_mouse_in()

def clica_bt2(event):
    print('Clicou no Botão.')

#*************************************************************************************************
#GUI
janela = Tk()
janela.geometry(resolucao)
janela.bind('<Key>', apertou_tecla)         #<Key> é o evento de precionar a tecla e chama a rotina
                                            #que tratará esse evento apertou_tecla()

lb1 = Label(janela, text='1) Aperte uma tecla e observe o console.')
lb2 = Label(janela, text='2) Aperte o botão direito do mouse.')
bt1 = Button(janela, text='3) Deixe o mouse sobre o botão e depois retire', width=50)
bt2 = Button(janela, text='4) Clique aqui', width=50)

janela.bind('<Button-3>', botao_direito)    #Evento de apertar o botão direito do mouse
bt1.bind('<Leave>', on_leave)               #Os eventos estão disponíveis também para os outros objetos
bt1.bind('<Enter>', on_enter)               #Evento de colocar o ponteiro do mouse sobre o objeto
bt2.bind('<Button-1>', clica_bt2)

#*************************************************************************************************
#Layout
lb1.grid(row=0, column=0, sticky=W)
lb2.grid(row=1, column=0, sticky=W)
bt1.grid(row=2, column=0, sticky=W)
bt2.grid(row=3, column=0, sticky=W)

#*************************************************************************************************
#Run
janela.mainloop()


