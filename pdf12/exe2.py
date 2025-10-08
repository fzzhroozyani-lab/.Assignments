import threading
arrInput = [2,3,4,7,6]
sq=[]
def square(num):
    square = num ** 2
    sq.append(square)
    
for number in arrInput:
    t=threading.Thread(target=square, args=(number,))
    t.start()
print(sq)