import socket
import datetime
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 1234))
s.listen(5)

try:
    clientsocket, address = s.accept()
    print(f'Connection from {address} has been established')

    msg = "Welcome to the server"
    clientsocket.send(bytes(msg, "utf-8"))

    while True:
        image_data = clientsocket.recv(2048)
        while image_data:
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
            file = open(f'server_img/{timestamp}.png', 'ab')
            file.write(image_data)
            image_data = clientsocket.recv(2048)
        file.close()
    clientsocket.close()

except:
    print('Client is disconnected!')