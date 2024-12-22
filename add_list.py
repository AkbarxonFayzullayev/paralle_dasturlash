import os
import time
from threading import Thread, current_thread
from multiprocessing import Process, current_process
from functools import reduce

def add_list(a:list):
    p_id = os.getpid()
    s_time = time.time()
    print(f"{p_id} --- {current_process().name} --- {current_thread().name} --- hisoblash boshlandi")
    toq = [a[element] for element in range(len(a)) if element%2==1]
    juft = [a[element] for element in range(len(a)) if element%2==0]
    result1 = reduce(lambda x, y: x * y, toq)
    result2 = reduce(lambda x, y: x * y, juft)
    print(result2 - result1)
    e_time = time.time()
    print(f"{p_id} --- {current_process().name} --- {current_thread().name} --- hisoblash tugadi --- Vaqt: {e_time - s_time}")
if __name__ == "__main__":
    list1 = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100]
    list2 = [100, 88, 99, 77, 66, 55, 44, 33, 22, 11]
    print("Single-thread boshlandi")
    s_time = time.time()
    add_list(list1)
    add_list(list2)
    e_time = time.time()
    print(f"Single-thread vaqt: {e_time - s_time}")
    print("Multi-thread boshlandi")
    s_time = time.time()
    t1 = Thread(target=add_list, args=(list1,))
    t2 = Thread(target=add_list, args=(list2,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    e_time = time.time()
    print(f"Multi-thread vaqt: {e_time - s_time} ")
    print("Multi-processing boshlandi")
    s_time = time.time()
    p1 = Process(target=add_list, args=(list1,))
    p2 = Process(target=add_list, args=(list2,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    e_time = time.time()
    print(f"Multi-processing vaqt: {e_time - s_time} ")
