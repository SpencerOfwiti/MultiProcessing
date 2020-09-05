import time
import multiprocessing
import os

arr = [2, 3, 4, 5]


def square(numbers):
    for n in numbers:
        time.sleep(2)
        print('Square : {0}, ProcessID : {1}'.format(n*n, os.getpid()))


def cube(numbers):
    for n in numbers:
        time.sleep(2)
        print('Cube : {0}, ProcessID : {1}'.format(n*n*n, os.getpid()))


print('Main process Id : {}'.format(os.getpid()))
t = time.time()
p1 = multiprocessing.Process(target=square, args=(arr,))
p2 = multiprocessing.Process(target=cube, args=(arr,))

p1.start()
p2.start()

p1.join()
p2.join()

print(time.time() - t)
print('Process 1 is alive : {}'.format(p1.is_alive()))
print('Process 2 is alive : {}'.format(p2.is_alive()))
