#************************************************************
#			MANIPULAÇÃO DE VARIÁVEIS DE AMBIENTE
#************************************************************
#(Linux)Adicionar no final do arquivo ~/.profile a linha
#export VAR_USER="Hello"
#após reiniciar com o mesmo usuário

#!/usr/bin/python3
import os

print("Lendo a variável.")
print(os.environ['VAR_USER'])		#ou os.environ.get('VAR_USER')

print("Escrevendo na variável.")
valor="Novo Valor"
os.environ['VAR_USER'] = valor

print("Lendo a variável novamente.")
print(os.environ['VAR_USER'])

