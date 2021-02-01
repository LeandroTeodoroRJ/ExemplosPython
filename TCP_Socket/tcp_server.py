# EXEMPLO SERVIDOR TCP PARA PYTHON

'''
Referências:
https://docs.python.org/3/library/socket.html
https://realpython.com/python-sockets/
'''

import socket
import time

servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#AF_INET -> Protocolo IP V4
#SOCK_TREAM -> TCP
#SOCK_DGRAM -> UDP

servidor.bind(('0.0.0.0', 1300))  #Escuta a porta 1300 da máquina local
servidor.listen()


while True:                            #While do deamon
    conn, addr = servidor.accept()     #conn é um objeto do tipo socket
    with conn:
        data = conn.recv(1024)         #Recebe máx 1024 bytes de buffer
        if not data:                   #Se não houver recepção de dados fecha o socket...
            conn.close()               #... mas continua ouvindo a porta
            continue
        else:
            conn.sendall(data)               #Devolve o dado para o cliente
            print('Recebido dados: ', data)
            print('Conectado ao IP: ', addr)
            time.sleep(10/1000)              #Delay de 10ms
            conn.close()                     #Finalizado a comunicação, fecha o soquete
