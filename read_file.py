import os
import time
from threading import Thread, current_thread
from multiprocessing import Process, current_process


def read_file(fayl):

    p_id = os.getpid()
    s_time = time.time()
    print(f"{p_id} --- {current_process().name} --- {current_thread().name} --- faylni o'qish boshlandi")
    with open(fayl, 'r') as file:
        text = file.read()
    e_time = time.time()
    print(
        f"{p_id} --- {current_process().name} --- {current_thread().name} --- faylni o'qish tugadi --- Vaqt: {e_time - s_time}")
    return text
if __name__ == "__main__":
    fayl1 = "text1.json"
    fayl2 = "text2.json"
    print("Single-thread boshlandi")
    s_time = time.time()
    read_file(fayl1)
    read_file(fayl2)
    e_time = time.time()
    print(f"Single-thread vaqt: {e_time - s_time}")
    print("Multi-thread boshlandi")
    s_time = time.time()
    t1 = Thread(target=read_file, args=(fayl1,))
    t2 = Thread(target=read_file, args=(fayl2,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    e_time = time.time()
    print(f"Multi-thread vaqt: {e_time - s_time} ")
    print("Multi-processing boshlandi")
    s_time = time.time()
    p1 = Process(target=read_file, args=(fayl1,))
    p2 = Process(target=read_file, args=(fayl2,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    e_time = time.time()
    print(f"Multi-processing vaqt: {e_time - s_time} ")