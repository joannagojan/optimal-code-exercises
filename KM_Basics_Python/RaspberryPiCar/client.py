import socket


host = socket.gethostbyname(socket.gethostname()) # as not using a VB
PORT = 9093

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.connect((host, PORT))

socket.send('Henlo server, this is the client'.encode('utf-8'))

print(socket.recv(1024).decode('utf-8'))

while True:
    receive_message = socket.recv(1024).decode('utf-8')
    print(f'Server message: {receive_message}')
    send_message = input('Input message to server: ')
    print(f'Sent message: {send_message}')
    socket.send(send_message.encode('utf-8'))


