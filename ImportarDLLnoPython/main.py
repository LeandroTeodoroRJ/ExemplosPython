#**********************************************************************
#                     IMPORTANDO DLL NO PYTHON
#**********************************************************************
'''
Neste exemplo uma função dentro de uma dll compilada no Delphi XE6
é chamada dentro do programa em Python.
Python Ver: 3.5.3 64-bits
'''
#OBS: Para evitar erros, compilar a DLL na versão do Python que
#está sendo utilizada: 32 ou 64-bits

import ctypes

dll = ctypes.WinDLL('DriveDLL.dll') #Carrega o arquivo dll
res = dll.somar(2, 3)    #Carrega a função que está no arquivo dll

print(res)

'''
https://docs.python.org/3/library/ctypes.html#calling-functions
16.16.1. ctypes tutorial
Note: The code samples in this tutorial use doctest to make sure that they 
actually work. Since some code samples behave differently under Linux, Windows, 
or Mac OS X, they contain doctest directives in comments.

Note: Some code samples reference the ctypes c_int type. On platforms where 
sizeof(long) == sizeof(int) it is an alias to c_long. So, you should not be 
confused if c_long is printed if you would expect c_int — they are actually the 
same type.

16.16.1.1. Loading dynamic link libraries
ctypes exports the cdll, and on Windows windll and oledll objects, for loading 
dynamic link libraries.

You load libraries by accessing them as attributes of these objects. cdll loads 
libraries which export functions using the standard cdecl calling convention, 
while windll libraries call functions using the stdcall calling convention. 
oledll also uses the stdcall calling convention, and assumes the functions 
return a Windows HRESULT error code. The error code is used to automatically 
raise an OSError exception when the function call fails.
'''