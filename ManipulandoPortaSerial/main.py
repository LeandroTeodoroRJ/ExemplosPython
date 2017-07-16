#*************************************************************************************************
#                                MANIPULANDO A PORTA SERIAL
#*************************************************************************************************
#http://pyserial.readthedocs.io/en/latest/shortintro.html
#http://pyserial.readthedocs.io/en/latest/pyserial_api.html

import serial

#CONFIGURAÇÃO
ser = serial.Serial('COM1')  #Abre a porta e configura
ser.baud = 9600
ser.parity = serial.PARITY_NONE
ser.stopbits = serial.STOPBITS_ONE
ser.bytesize = serial.EIGHTBITS
ser.timeout = 1

ser2 = serial.Serial('COM2') #Pode controlar múltiplas conexões

print(ser.name)             # check which port was really used

#ENVIAR BYTES
#ser.write(b'hello')        #Envia uma string pela porta serial

hexa_num = '0F'             #Envia um byte em hexa
dado = bytes.fromhex(hexa_num)

dec_num = 55                #Enviar um byte em decimal
dado = bytes([dec_num])
ser.write(dado)

#RECEBER BYTES
#line = ser2.read()          #Lê 1 byte
#line = ser2.read(10)        #Lê 10 bytes
#line = ser2.readline()      #Lê o caractere '\n' e interpreta como quebra de linha
line = ser2.read_all()       #Lê todos os bytes
#print(line)                 #Imprime em formato string
print(int.from_bytes(line, byteorder='big'))     #Converte Bytes para inteiro

ser.close()                  #Fecha a porta
ser2.close()


'''
Função serial.Serial()
Parameters:
    port – Device name or None.
    baudrate (int) – Baud rate such as 9600 or 115200 etc.
    bytesize – Number of data bits. Possible values: FIVEBITS, SIXBITS, SEVENBITS, EIGHTBITS
    parity – Enable parity checking. Possible values: PARITY_NONE, PARITY_EVEN, PARITY_ODD PARITY_MARK, PARITY_SPACE
    stopbits – Number of stop bits. Possible values: STOPBITS_ONE, STOPBITS_ONE_POINT_FIVE, STOPBITS_TWO
    timeout (float) – Set a read timeout value.
    xonxoff (bool) – Enable software flow control.
    rtscts (bool) – Enable hardware (RTS/CTS) flow control.
    dsrdtr (bool) – Enable hardware (DSR/DTR) flow control.
    write_timeout (float) – Set a write timeout value.
    inter_byte_timeout (float) – Inter-character timeout, None to disable (default).

Raises:
    ValueError – Will be raised when parameter are out of range, e.g. baud rate, data bits.
    SerialException – In case the device can not be found or can not be configured.

'''
