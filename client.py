import socket

handlerSocket = socket.socket()
serverIP = '127.0.0.1'
serverPort = 2222

handlerSocket.connect((serverIP,serverPort))
print('Live chat ready')

while True:
    message = handlerSocket.recv(1024)
    print('Pesan Dokter :',message.decode())
    pesan_pasien = [message.decode()]
    message = str(input('Masukkan pesan anda : '))
    handlerSocket.send(message.encode())