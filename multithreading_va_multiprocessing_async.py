from time import sleep
import os
import time
from threading import Thread, current_thread
from multiprocessing import Process, current_process

count = 100000000
sleep = 10
def io_b(sec):
    p_id = os.getpid()
    print(f"{p_id} --- {current_process().name} --- {current_thread().name} --- kutish boshlandi")
    time.sleep(sleep)
    print(f"{p_id} --- {current_process().name} --- {current_thread().name} --- kutish yakunlandi")

def cpu_b(k):
    p_id = os.getpid()
    print(f"{p_id} --- {current_process().name} --- {current_thread().name} --- hisoblash boshlandi")
    while k > 0:
        k-=1
    print(f"{p_id} --- {current_process().name} --- {current_thread().name} --- hisoblash yakunlandi")

if __name__ == "__main__":
    s_time = time.time()
    #1.singlethreed io_b
    io_b(sleep)
    io_b(sleep)

    # 1.multithreed
    t1 = Thread(target=io_b,args=(sleep,))
    t2 = Thread(target=io_b,args=(sleep,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    # 4.multithreed
    t1 = Thread(target=cpu_b, args=(sleep,))
    t2 = Thread(target=cpu_b, args=(sleep,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    # 2.singlethread

    cpu_b(count)
    cpu_b(count)
    # 5.multiprocessing
    p1 = Process(target=io_b,args=(sleep,))
    p2 = Process(target=io_b,args=(sleep,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    # 4.singleprocessing
    p1 = Process(target=cpu_b,args=(sleep,))
    p2 = Process(target=cpu_b,args=(sleep,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    e_time = time.time()



    print("Vaqt =",e_time - s_time)