from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import time
from person import Person


BUFSITZ = 512

HOST = 'localhost'
PORT = 32000
persons = []
ADDR = (HOST, PORT)
MAX_CONNECTION = 5
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)


def broadcast(msg, name):
    for person in persons:
        client = person.client
        try:
            client.send(bytes(name, "utf8") + msg)
        except Exception as e:
            print("[EXCEPTION]", e)

def client_komonikasi(person):
    client = person.client

    name = client.recv(BUFSITZ).decode("utf8")
    person.set_name(name)
    msg = bytes(f"{name} has joined the chat ", "utf8")
    broadcast(msg, "")
    while True:
        try:
            msg = client.recv(BUFSITZ)
            
            if msg == bytes("{quit}", "utf8"):
                client.send(bytes("{quit}", "utf8"))
                client.close()
                broadcast(bytes(f"{name} sudah meninggalkan Obrolan", "utf8"), "")
                persons.remove(person)
                print(f"[DISCONNECTED] {name} disconnected")
                break
            else:
                broadcast(msg, name + ': ')
                print(f"{name}: ", msg.decode("utf8"))
        except Exception as e:
            print("[EXCEPTION]", e)
            break


        


def Menunggu_koneksi(self):
    while True:
        try:
            client, addr = SERVER.accept()
            person = Person(addr, client)
            persons.append(person)
            print(f"[Connection] {addr} koneksi ke dalam server pada waktu{time.time()}")
            Thread(target=client_komonikasi, args=(person,)).start()
        except Exception as e:
            print("[EXCEPTION]", e)
            break
    print("Server Rusak")





if __name__ == "__main__":
    SERVER.listen(5)
    print("[STARTTED]Menungu Koneksi..")
    ACCEPT_THREAD = Thread(target=Menunggu_koneksi, args=(SERVER, ))
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()