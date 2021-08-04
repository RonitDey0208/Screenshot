import socket
from time import sleep
import datetime
import random
import pyautogui
import time


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost',1234))

msg = s.recv(1024).decode()
print(msg)

while True:
    ss = pyautogui.screenshot()
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    ss.save(f'{timestamp}.png')

    file = open(f'{timestamp}.png', 'rb')
    image_data = file.read()
    s.sendall(image_data)

    file.close()
    sleep(3)

s.close()