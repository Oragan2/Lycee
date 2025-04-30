import socket
import threading

<<<<<<< HEAD
HOST = '10.0.0.37'
=======
HOST = '127.0.0.1'
>>>>>>> fc9acc5024275baf41e857549168f97a380f1a0b
PORT = 9999

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.bind((HOST,PORT))

serveur.listen(5)

clients = []
nicknames = []

def broadcast(message:str):
    for client in clients:
        client.send(message)

def handle(client:socket):
    while True:
        try:
            message = client.recv(1024)
            if message == f'{nicknames[clients.index(client)]} has disconected'.encode():
                broadcast(message)
                raise BrokenPipeError
            elif message != b'':
                print(f"{message.decode()}")
                broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nicknames.pop(index)
            break
    
def receive():
    while True:
        client, address = serveur.accept()
        print(f"Connected with {str(address)}")
        
        nickname = client.recv(1024).decode()
        
        clients.append(client)
        nicknames.append(nickname)
        
        print(f"Nickname of the client is {nickname}")
        broadcast(f"{nickname} has connected to the serveur.\n".encode())
        client.send("Connected to the serveur".encode())
        
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()      

print("Serveur running...")
receive()