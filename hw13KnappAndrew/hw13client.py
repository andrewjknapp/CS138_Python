# client.py  
import socket

def main():
    promptAgain = True
    while promptAgain:
        phrase = input("Please enter a phrase: ")

        sendRequest(phrase)

        promptAgain = input("Enter another phrase? (y/n) ") == 'y' 

def sendRequest(phrase):

    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    # get local machine name
    # host = socket.gethostname()  
    host = '127.0.0.1'                         

    port = 9999

    # connection to hostname on the port.
    s.connect((host, port))    

    s.send(phrase.encode())                           

    # Receive no more than 1024 bytes
    message = s.recv(1024).decode()                               

    s.close()

    print(f"The reverse of that phrase is: {message}")


if __name__ == '__main__':
    main()