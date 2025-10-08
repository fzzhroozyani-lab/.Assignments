import threading
import time

wallet=100
lock =threading.Lock()
def add_money():
    global wallet
    with lock:
        wallet2=wallet
        time.sleep(2)
        wallet = wallet2+10
        print("walllet now",wallet)

treads=[]  
for money in range(0,10):
    t=threading.Thread(target=add_money)
    treads.append(t)
    t.start()
for i in treads:
    t.join()
print(wallet)