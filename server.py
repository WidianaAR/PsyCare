import socket

listenersocket = socket.socket()
serverIP = '0.0.0.0'
serverPort = 2222
listenersocket.bind((serverIP,serverPort))
listenersocket.listen(0)
print('Server ready')

while True:
    handlerSocket, addr = listenersocket.accept()
    print('Terhubung',addr)
    while True:
        message = input('Masukkan pesan : ')
        handlerSocket.send(message.encode())
        message = handlerSocket.recv(1024)
        string = message.decode()
        pesan_dokter = [message.decode()]
        print('Pesan pasien :',message.decode())