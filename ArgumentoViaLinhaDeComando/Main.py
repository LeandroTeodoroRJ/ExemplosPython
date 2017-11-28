#*****************************************************************************************
#                       PASSANDO ARGUMENTOS VIA LINHA DE COMANDO
#*****************************************************************************************
#Para teste chamar como: python Main.py Param1 Param2

import sys
print(sys.argv[0])      #Primeiro elemento da lista é sempre o nome do programa em python
print(sys.argv[1])      #Primeiro argumento passado pela linha de comando
print(sys.argv[2])      #Segundo argumento passado pela linha de comando
print("Total de argumentos: %s" %len(sys.argv)) #Tamanho da lista (Quantidade de argumentos)
print('\n')
print('Todos os argumentos passados')
for param in sys.argv:
    print(param)
