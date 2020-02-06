# Brian Spencer
# CSC 460
# 2/6/2020

from socket import *
import threading

# variable to tell server to exit
keepRunning = True

# define a function to handle a single client
def client(clientSocket):
	while True:
		# get a message from the client
		move = clientSocket.recv(1024).upper()
		
		# empty - Assume the client has disconnected
		if len(move) == 0:
			return
		if move == "Q":
			print('A player chose to quit. Server shutting down.')
			keepRunning = False
			return
	
		# update
		clientSocket.send(theirHand)
		clientSocket.send(currValue)
		clientSocket.send(currSuit)
	# end function client()

# function to handle the main server socket accept loop
def listenLoop(svrPort):
	# create the socket
	serverSocket = socket( AF_INET, SOCK_STREAM )
	serverSocket.bind( ('',serverPort) )
	#number of cleints
	serverSocket.listen(2)

	print('The server is ready to receive')
	while keepRunning:
		# get a connection from a client
		connectionSocket, addr = serverSocket.accept()
		
		# start up a thread for that client
		cl = threading.Thread( target=client, args=(connectionSocket,), daemon=True )
		cl.start()

svrPort = int(input('Enter port number for the server: ' ))

#start a thread for each client that connects
sthread = threading.Thread( target=listenLoop, args=(svrPort,), daemon=True )
sthread.start()