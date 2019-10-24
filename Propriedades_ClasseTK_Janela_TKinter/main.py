#*************************************************************************************************
#                            PROPRIEDADES DA CLASSE TK() - JANELA
#*************************************************************************************************
#Descomente as linhas de código e rode para ver os resultados
#
#*************************************************************************************************
#INCLUDES
from tkinter import*
from tkinter.ttk import*
from main_code import *             #Módulo do arquivo de código
from janela2 import *               #Módulo da janela 2
#*************************************************************************************************
#CONSTANTES E DEFINIÇÕES
resolucao = '600x200+200+200'
#resolucao = '800x600+1+1'          #Resolução de 800x600 orientado no canto superior esquerdo
                                    #Para encostar totalmente coloque 0+0

#*************************************************************************************************
#EVENTOS
def apertou_tecla(event):                           #Função do evento de apertar a tecla
    trata_tecla(event.char, event.keycode)

def clica_bt2(event):                               #O parâmetro event deve ser passado obrigatoriamente
    janela.destroy()

def clica_bt1(event):
    abre_janela2()
#*************************************************************************************************
#GUI
janela = Tk()
janela.geometry(resolucao)
#janela.resizable(0, 0)          #Não permite redimensionar a janela e desabilita botão de maximizar
#janela.overrideredirect(1)       #Remove os botões da janela e não permite redimensonar
#janela['bg'] = 'Black'           #Altera a cor de fundo da janela

janela.bind('<Key>', apertou_tecla)         #<Key> é o evento de precionar a tecla e chama a rotina
                                            #que tratará esse evento apertou_tecla()

lb1 = Label(janela, text='Propriedades da classe Tk().')
bt2 = Button(janela, text='Fechar Janela', width=50)
bt1 = Button(janela, text='Abrir nova Janela', width=50)
bt2.bind('<Button-1>', clica_bt2)
bt1.bind('<Button-1>', clica_bt1)

#*************************************************************************************************
#Layout
lb1.grid(row=0, column=0, sticky=W)
bt2.grid(row=1, column=0, sticky=W)
bt1.grid(row=2, column=0, sticky=W)

#*************************************************************************************************
#Run
janela.mainloop()


