######################################################
#        Programa principal em Python
######################################################
import os		#Importa módulo 
var="Param1"	#Parâmetro que será passado para o shell
os.system("./LinuxScript.sh %s" %var) #Chamada do script com o parâmetro
