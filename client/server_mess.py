import socket
import threading
import time


def save_ip_to_file(ip_):
    txt = open('ip.txt', 'w')
    txt.write(ip_)
    txt.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
ip = socket.gethostbyname(host)

save_ip_to_file(ip)
port = 9090
server.bind((ip, port))
server.listen(3)
server.settimeout(0.2)
print('{exit} for exit')

clients = list()

end = list()

outdata = ''


def accept():
    while True:
        try:
            client, addr = server.accept()
            #            print('123213213213')
            #            print(client)
            clients.append(client)
            print(f'Server connect to {addr}: online now: ----- {len(clients)}')
        except socket.timeout:
            if outdata == 'exit':
                break


def recv_data(client):
    while True:
        try:
            indata = client.recv(1024)
        except Exception as k:
            #            print(clients)
            #            print(client)
            clients.remove(client)
            end.remove(client)
            print(f'Client off: now online: ----- {len(clients)}')
        print(indata.decode('utf-8'))
        for cl in clients:
            if cl != client:
                cl.send(indata)


def outdatas():
    while True:
        global outdata
        outdata = input()
        if outdata == 'exit':
            break
        #        if outdata == 'check':
        #           print(threading.enumerate())
        #           print(threading.active_count())
        print('Send all:% s' % outdata)
        for cl in clients:
            cl.send(f"Server: {outdata}".encode('utf-8)'))


def indatas():
    while True:
        if outdata == 'exit':
            break
        for cl in clients:
            if cl in end:
                continue
            index = threading.Thread(target=recv_data, args=(cl,))
            index.start()
            end.append(cl)


t2 = threading.Thread(target=outdatas, name='out')
t2.start()

# Input data
t1 = threading.Thread(target=indatas, name='input')
t1.start()

# Send data

# Client waiting
t3 = threading.Thread(target=accept, name='accept')
t3.start()

# print(clients)
# print(threading.enumerate())
# print(threading.active_count())

t2.join()

for client in clients:
    client.close()

print('-' * 5 + 'сервер отключен' + '-' * 5)
# print(threading.enumerate())
# print(threading.active_count())
# print(outdata)
