#*************************************************************************************************
#                                  EVENTOS - ARQUIVO DE CÓDIGO
#*************************************************************************************************

def trata_tecla(tecla, codigo):                     #Função do evento de apertar a tecla
    print('Você apertou a tecla:', tecla)           #Retorna o tecla precionada
    print('O código da tecla é:', codigo)           #Retorna os códigos das teclas, inclusive
                                                    #as teclas de função.
def trata_direito():                                #O parâmetro event deve ser passado obrigatoriamente
    print('Você apertou o botão direito do mouse')
    return 'Evento ativado'

def trata_mouse_out():
    print('Você retirou o mouse do botão')

def trata_mouse_in():
    print('Você está com o mouse em cima do botão')



