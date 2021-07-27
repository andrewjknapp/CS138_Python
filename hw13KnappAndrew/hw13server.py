# hw13server.py 
import socket                                         
import time

# create a socket object
serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
# host = socket.gethostname()  
host = '127.0.0.1'                         

port = 9999                                           

# bind to the port
serversocket.bind((host, port))                                  

# queue up to 5 requests
serversocket.listen(5)                                           
print(f"Server listening on port {port}")

while True:
    # establish a connection
    clientsocket,addr = serversocket.accept()   
    print("Got a connection from %s" % str(addr)) 

    # Get message from client
    recvData = clientsocket.recv(1024).decode()  
    print(f"Phrase received: {recvData}")

    # Send reverse of the message sent
    clientsocket.send(recvData[::-1].encode())

    clientsocket.close()
