#!/usr/bin/env python

import socket
#server
 
host_name = socket.gethostname() 
host_ip = socket.gethostbyname(host_name)

TCP_IP = host_ip

TCP_PORT = 5005

BUFFER_SIZE = 1024

MESSAGE = "Hello, World!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(2)

print(TCP_IP)

while True:
    conn, addr = s.accept()
    data = conn.recv(BUFFER_SIZE)
    if not data: 
        break
    print("received data: ", data)
    conn.send(data)  # echo
  
conn.close()
