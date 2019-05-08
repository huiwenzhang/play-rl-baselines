"""
Demo script used for learning basic concepts processing and thread
in python.
"""

from multiprocessing import Process, Pool, Queue, Pipe
import os, time, random
import threading


def run_proc(name):
    print("Run child process {} with pid {}".format(name, os.getpid()))


def long_time_task(name):
    print("Run task {} in process {}".format(name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print("Task {} run for {} seconds".format(name, end - start))


# communiccation between processes
# write and read from the same memory
def write(q):
    """

    :param q: the Quene object
    :return:
    """
    print("Write data into Quene object in process {}".format(os.getpid()))
    for value in ['A', 'B', 'C']:
        print("Put {} to quene ...".format(value))
        q.put(value)
        time.sleep(random.random())


def read(q):
    """
    read data from quene
    :param q: target quene
    :return:
    """
    print("Read data from quene in process {}".format(os.getpid()))
    while True:
        value = q.get(True)
        print("Read %s from quene." % value)


def loop():
    """
    fuction executed in a thread
    :return:
    """
    print("Thread {} is running ...".format(threading.current_thread().name))
    n = 0
    while n < 5:
        n += 1
        print("Thread {} >>> {}".format(threading.current_thread().name, n))
        time.sleep(1)
    print("Thread {} is over".format(threading.current_thread().name))


print("==============================================")
print("Parent process {}".format(os.getpid()))
sub_proc = Process(target=run_proc, args=('test_code',))
print("Child process will start")
sub_proc.start()
# wait for the termination of the  sub-process and contiune
sub_proc.join()
print("Subprocess closed")

# example for using process pool
print("===============================================")
print("Test Pool class")
p = Pool(4)
for i in range(5):
    p.apply_async(long_time_task, args=(i,))
print("Wait until all sub-processes are done")
p.close()
p.join()
print("Done")

print("================================================")
print("Communication between two  processes")
# Create a quene in parent process
q = Queue()
write_quene = Process(target=write, args=(q,))
read_quene = Process(target=read, args=(q,))

write_quene.start()
read_quene.start()
# terminate when subprocess is done
write_quene.join()
read_quene.terminate()

print("=================================================")
print("Thread demo")
# _thread is low-level module
# threading is high-level module
print("Thread {} is running ...".format(threading.current_thread().name))
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print("Thread {} is over ...".format(threading.current_thread().name))

print("======================LOCK=========================")
"""
The major differences between thread and process are:
in multiple process, for the same variable, each process with copy the variable and 
store it in its own process. However, in multiple threads, they share the same variable
and memory, so if whichever the thread changes the variable, it will affect other threads 
"""
print("Demo to show shared variable in multiple threads")
# your money
balance = 0


def change(n):
    global balance
    balance += n
    balance -= n
    # print(n)


def run_thread(n):
    for i in range(100000):
        change(n)


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

"""
We see that two thread operate on the same variable balance, so
the value is uncontrolable. To solve this, we lock the change() func
so that each second only one thread can change the value
"""
balance = 0
lock = threading.Lock()


def lock_thread(n):
    for i in range(10000):
        lock.acquire()
        try:
            change(n)
        finally:
            lock.release()


t1 = threading.Thread(target=lock_thread, args=(5,))
t2 = threading.Thread(target=lock_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
