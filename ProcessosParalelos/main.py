#*************************************************************************************************
#                                   PROCESSOS PARALELOS
#*************************************************************************************************
'''
Objetivo: Rodar um processo paralelo por trás da caixa de mensagem. Note que sem o processo
paralelo, só seria possível a impressão no console (linha 24) após o fechamento da caixa de mensagem
(linha 21), já que o programma ficaria parado até isso cocorrer.
'''


#INCLUDES
from tkinter import*
from tkinter.ttk import *
import tkinter.messagebox
import _thread                      #Importa o módulo de processamento paralelo

#CONSTANTES E DEFINIÇÕES
resolucao = '300x300+200+200'
#FUNÇÕES
def tarefa_paralela(texto):
    tkinter.messagebox.showinfo('Tarefa Paralela', 'Texto da caixa: %s' %(texto))

def tarefa_paralela2(texto):
    print(texto)

def clica_botao():
    _thread.start_new_thread(tarefa_paralela, ('mensagem 1',))
    _thread.start_new_thread(tarefa_paralela2, ('Tarefa paralela no console.',))
    print('Processo principal.')

#GUI
janela = Tk()
janela.geometry(resolucao)
bt1 = Button(janela, width=20, text='Inicicar', command=clica_botao)

#Layout
bt1.place(x=100,y=100)
janela.mainloop()

'''
OBS: Após o encerramento do processo principal todos os processos paralelos
são automaticamente encerrados, mesmo que ainda abertos.
'''
