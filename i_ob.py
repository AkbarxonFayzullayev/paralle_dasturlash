import json
import os
import time
from threading import  current_thread
from multiprocessing import  current_process


def read_file(fayl1):

    p_id = os.getpid()
    print(f"{p_id} --- {current_process().name} --- {current_thread().name} --- faylni o'qish boshlandi")
    with open(f"{fayl1}", 'r') as file:
        text1 = file.read()
    print(f"{p_id} --- {current_process().name} --- {current_thread().name} --- faylni o'qish tugadi")

    return text1

if __name__ == "__main__":
    s_time = time.time()
    read_file("text1.json")
    read_file("text2.json")

    e_time = time.time()



    print("Vaqt =",e_time - s_time)
