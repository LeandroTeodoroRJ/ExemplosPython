#*************************************************************************************************
#                                        JANELA2.PY
#*************************************************************************************************
# Arquivo do GUI referente a janela2
#
# *************************************************************************************************
# INCLUDES
from tkinter import *
from tkinter.ttk import *
from janela2_code import *
#*************************************************************************************************

def abre_janela2():
    #Cuidado com o espaçamento
    #CONSTANTES E DEFINIÇÕES
    resolucao_j2 = '600x200+200+200'


    #*************************************************************************************************
    #EVENTOS
    def clica_bt2(event):
        janela2.destroy()

    def clica_bt1(event):
        trata_bt()

    #*************************************************************************************************
    #GUI
    janela2 = Tk()
#    janela2.overrideredirect(1)        #Abre a janela sem botões em formato Show Modal sem redimensionamento
    janela2.geometry(resolucao_j2)

    lb1 = Label(janela2, text='Janela 2.')
    bt2 = Button(janela2, text='Fechar Janela', width=50)
    bt1 = Button(janela2, text='Evento Clica Botão', width=50)
    bt2.bind('<Button-1>', clica_bt2)
    bt1.bind('<Button-1>', clica_bt1)

    #*************************************************************************************************
    #Layout
    lb1.grid(row=0, column=0, sticky=W)
    bt2.grid(row=1, column=0, sticky=W)
    bt1.grid(row=2, column=0, sticky=W)

    #*************************************************************************************************


