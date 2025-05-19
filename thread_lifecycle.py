
import threading
import time

def task():
    print(" threading stated....") 
    time.sleep(5)
    print(" threading finished....") 
    time.sleep(3)

if __name__=="__main__":
    t=threading.Thread(target=task)
    print("threading state :", t.is_alive())
    t.start()
    print("threading state after start : ",t.is_alive())
    t.join()
    print("threading state after join : ", t.is_alive())          

     