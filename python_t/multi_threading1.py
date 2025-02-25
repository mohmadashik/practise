import threading
import time 

def cubes(x,y):
    for i in range(x):
        print(f'{i}**3 is {i**3}')
        time.sleep(0.01)
    
def squares(x,y):
    for i in range(x):
        print(f'{i}**2 is {i**2}')
        time.sleep(0.01)

t1 = threading.Thread(target=cubes,args=[5,10])
t2 = threading.Thread(target=squares,args=[5,10])
# t3 = threading.Thread(target=func_name,args=[6,36])
t1.start()
t2.start()
# t3.start()
# The GIL (Global Interpreter Lock) ensures that only one thread can execute Python bytecode at a time.
# This prevents multiple threads from accessing Python objects simultaneously, ensuring safe memory management.
# The GIL is released during I/O operations (e.g., time.sleep(), file reads, or network requests),
# allowing other threads to acquire the lock and execute their tasks.
# The switching time between threads is extremely short (microseconds), creating the illusion of parallelism.
# However, true parallel execution is not possible for CPU-bound tasks in CPython due to the GIL.
