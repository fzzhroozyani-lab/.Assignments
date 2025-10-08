import threading
import time
arrInput = [40, 5, 30, 9, 42]
def check(num):
    if num < 10:
        print(num)
    time.sleep(1)
start= time.time()
treads=[]
for number in arrInput:
    t=threading.Thread(target=check, args=(number,))
    treads.append(t)
    t.start()
for t in treads:
    t.join()
end=time.time()
print (end-start)