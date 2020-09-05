import multiprocessing


def square_list(mylist, result, square_sum):
    for idx, num in enumerate(mylist):
        result[idx] = num * num

    square_sum.value = sum(result)

    print('Result in process 1 : {}'.format(result[:]))
    print('Sum of squares in process 1 : {}'.format(square_sum.value))


if __name__ == '__main__':
    mylist = [1, 2, 3, 4]

    result = multiprocessing.Array('i', 4)
    square_sum = multiprocessing.Value('i')

    p1 = multiprocessing.Process(target=square_list,
                                 args=(mylist, result, square_sum))

    p1.start()
    p1.join()

    print('Result in main process : {}'.format(result[:]))
    print('Sum of squares in main process : {}'.format(square_sum.value))
