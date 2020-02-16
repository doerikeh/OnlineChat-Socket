from socket import AF_INET, SOCK_STREAM, socket
from threading import Thread

HOST = 'localhost'
PORT = 32000

ADDR = (HOST, PORT)
BUFSITZ = 512

messages = []
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

def receive_message():
    while True:
        try:
            msg = client_socket.recv(BUFSITZ).decode()
            messages.append(msg)
            print(msg)
        except Exception as e:
            print("[EXCEPTION]", e)
            break


def send_messages(msg):
    client_socket.send(bytes(msg, encoding='utf8'))
    if msg == "{quit}":
        client_socket.close()


receive_thread = Thread(target=receive_message)
receive_thread.start()


send_messages("Ike")
send_messages("hello")