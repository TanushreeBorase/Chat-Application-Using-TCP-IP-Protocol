import socket
import threading

# Server setup
HOST = '127.0.0.1'  # Localhost
PORT = 12345        # Port for the server

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
nicknames = []

# Broadcast message to all clients
def broadcast(message):
    for client in clients:
        client.send(message)

# Handle client messages
def handle_client(client):
    while True:
        try:
            # Receive and broadcast message
            message = client.recv(1024)
            broadcast(message)
        except:
            # Remove client if error occurs
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat!'.encode('utf-8'))
            nicknames.remove(nickname)
            break

# Accept connections from multiple clients
def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        # Ask for nickname
        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print(f'Nickname of the client is {nickname}')
        broadcast(f'{nickname} joined the chat!'.encode('utf-8'))
        client.send('Connected to the server!'.encode('utf-8'))

        # Start a new thread for each client
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

print('Server is listening...')
receive()
