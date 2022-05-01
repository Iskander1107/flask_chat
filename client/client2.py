import socket
import threading
import time

import requests
import config

address = 'http://127.0.0.1:5000/'
# email = 'iskander@gmail.com'
# password = '123'


def get_ip():
    txt = open('ip.txt', 'r')
    ip = txt.readline()
    return ip


def check(email, password):
    name = requests.get(address + 'getlog' + f'?email={email}&password={password}').text
    if name == 'error':
        return None
    return name


while True:
    email = input('Enter email')
    password = input('Enter password')
    name = check(email, password)
    if name is not None:
        break


print(f"Hello, {name}")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

name = check(email, password)

port = 9090

client.connect((get_ip(), port))

print('{exit} for exit')

outdata = ''


def outdatas():
    while True:
        outdata = input()
        if outdata == 'exit':
            time.sleep(0.5)
            break
        client.send(f'{name}:{outdata}'.encode('utf-8'))
        print('%s:%s' % (name, outdata))


def indatas():
    while True:
        try:
            indata = client.recv(1024)
        except Exception:
            break
        print(indata.decode('utf-8'))


t1 = threading.Thread(target=indatas, name='input')

t2 = threading.Thread(target=outdatas, name='out')

t1.start()
t2.start()

t2.join()


client.close()

t1.join()
print('Server off')
