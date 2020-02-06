# Brian Spencer
# CSC 460
# 2/6/2020

from socket import *

svrIP = input('Enter your local IP address: ')
svrPort = int(input('Enter the port number of server: ' ))

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(svrIP, svrPort)

print('To select a card, type the value and suit together.')
print('Some examples and special cases: ')
print('1C means "Ace of Clubs"; 8S means "Eight of Spades"; 13H means "King of Hearts"')

# take user input as long as it's their turn
while turn:
    msg = input('Play a card or draw: ')
    if msg == '^C':
        break;
    clientSocket.send(message.upper())

clientSocket.close()
