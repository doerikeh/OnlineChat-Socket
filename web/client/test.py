from client import Clinet
import time
from threading import Thread

c1 = Clinet("")
c2 = Clinet("")



def update_pesan():
    msgs = []
    run = True
    while run:
        time.sleep(1)
        new_pesan = c1.get_messages()
        msgs.extend(new_pesan)
        for msg in new_pesan:
            print(msg)
            if msg == "{quit}":
                run = False
                break


Thread(target=update_pesan).start()

c1.send_messages("hai")
c2.send_messages("hai juga")
time.sleep(1)
c1.send_messages("Ada Apa nih")
time.sleep(2)
c2.send_messages("ada berita baru")


c1.disconnected()
time.sleep(2)
c2.disconnected()
time.sleep(2)
