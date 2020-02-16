from socket import AF_INET, SOCK_STREAM, socket
from threading import Thread

HOST = 'localhost'
PORT = 32000

ADDR = (HOST, PORT)
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()