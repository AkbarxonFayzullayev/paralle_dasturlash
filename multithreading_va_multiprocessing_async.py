import os
import time
from threading import Thread, current_thread
from multiprocessing import Process, current_process

count = 100_000_000
sleep = 10


def io_b(sec):
    p_id = os.getpid()
    print(f"{p_id} --- {current_process().name} --- kutish boshlandi")
    time.sleep(sec)
    print(f"{p_id} --- {current_process().name} --- kutish yakunlandi")


def cpu_b(k):
    p_id = os.getpid()
    print(f"{p_id} --- {current_process().name} --- hisoblash boshlandi")
    while k > 0:
        k -= 1
    print(f"{p_id} --- {current_process().name} --- hisoblash yakunlandi")


if __name__ == "__main__":
    s_time = time.time()

    # 1. Single-thread I/O
    io_b(sleep)
    io_b(sleep)

    # 2. Multi-threaded I/O
    t1 = Thread(target=io_b, args=(sleep,))
    t2 = Thread(target=io_b, args=(sleep,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    # 3. Multi-threaded CPU
    t1 = Thread(target=cpu_b, args=(count,))
    t2 = Thread(target=cpu_b, args=(count,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    # 4. Single-threaded CPU
    cpu_b(count)
    cpu_b(count)

    # 5. Multi-processing I/O
    p1 = Process(target=io_b, args=(sleep,))
    p2 = Process(target=io_b, args=(sleep,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    # 6. Multi-processing CPU
    p1 = Process(target=cpu_b, args=(count,))
    p2 = Process(target=cpu_b, args=(count,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    e_time = time.time()
    print("Vaqt =", e_time - s_time)
