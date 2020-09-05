import multiprocessing
import os


def square(n):
    print('Worker process ID for {0} : {1}'.format(n, os.getpid()))
    return n*n


if __name__ == '__main__':
    mylist = [1, 2, 3, 4, 5]

    p = multiprocessing.Pool()

    result = p.map(square, mylist)

    print(result)
