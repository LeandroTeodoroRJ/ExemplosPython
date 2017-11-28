#*************************************************************************************************
#                            MANIPULANDO ARQUIVOS DE CONFIGURAÇÃO - INI
#*************************************************************************************************
import configparser

config = configparser.ConfigParser()
config2 = configparser.ConfigParser()           #Segundo objeto instanciado somente para fins didáticos

config.add_section('section1')                  #Cabeçalho
config.set('section1', 'user', 'Leandro')       #Opção<user> - Value<leandro>
config.set('section1', 'pass', '1234')

config.add_section('section2')
config.set('section2', 'config_user', '1')

with open('config.ini', 'w') as configfile:
    config.write(configfile)                    #Grava o arquivo

config2.read('config.ini')                      #Leitura do arquivo
print(config2.get('section1', 'user'))          #Lê como string
print(config2.getint('section1', 'pass'))       #Lê como inteiro (já faz o cast), também funcionaria com o get()
print(config2.getint('section2', 'config_user'))

"""
Espelho do arquivo config.ini
[section1]
user = Leandro
pass = 1234

[section2]
config_user = 1
"""


