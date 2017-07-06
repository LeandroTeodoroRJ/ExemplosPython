#**********************************************************************
#                     IMPORTANDO DLL NO PYTHON
#**********************************************************************
'''
Neste exemplo uma função dentro de uma dll compilada no Delphi XE6
é chamada dentro do programa em Python.
Python Ver: 3.5.3
'''
#OBS: Para evitar erros, compilar a DLL na versão do Python que
#está sendo utilizada: 32 ou 64-bits

import ctypes

dll = ctypes.WinDLL('DriveDLL.dll') #Carrega o arquivo dll
res = dll.somar(2, 3)    #Carrega a função que está no arquivo dll

print(res)
