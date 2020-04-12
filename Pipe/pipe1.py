#******************************************************************************
#               TRANSFERÊNCIA INTERNA DE DADOS VIA PIPE
#******************************************************************************
'''
Pipes são túneis que ligam de um lado o standard input e do outro lado o
standart output. Essa conexão é intermediada por um arquivo que nesse caso
é alocado temporariamente na memória.
'''

#!/usr/bin/python
import os

pipein, pipeout = os.pipe()

#Escrevendo
# Write one string
str = "Teste Pipe"                              #String que será transmitida pelo pipe
num = os.write(pipeout, str.encode())           #Cast de string para Bytes String
print("Número de bytes transmitidos: ", num)
print ("Dados transmitidos pelo pipe.")

#Lendo
# Reading text
ret = os.read(pipein, 12)           #Lê 12 bytes do pipe
print (ret.decode())                #Cast de Bytes String para String
print ("Dados lidos pelo pipe.")