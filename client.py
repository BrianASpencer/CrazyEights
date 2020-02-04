#!/usr/bin/env python

import socket
#client

host_name = socket.gethostname() 
host_ip = socket.gethostbyname(host_name)

TCP_IP = '157.89.5.95'

TCP_PORT = 5005

BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((TCP_IP, TCP_PORT))

while True:
    g = input("Enter something to tell the server: ") 
    msg = "my message is: "+str(g)
    MESSAGE = bytes(msg, 'utf-8')
    s.send(MESSAGE)
    data = s.recv(BUFFER_SIZE)
