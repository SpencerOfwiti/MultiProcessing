import multiprocessing


def sender(conn, msgs):
    for msg in msgs:
        conn.send(msg)
        print('Sent the message {}'.format(msg))
    conn.close()


def reciever(conn):
    while 1:
        msg = conn.recv()
        if msg == 'END':
            break
        print('Recieved the message {}'.format(msg))


if __name__ == '__main__':
    msgs = ['Hello', 'Hey', 'Holla', 'END']

    parent_conn, child_conn = multiprocessing.Pipe()

    p1 = multiprocessing.Process(target=sender, args=(parent_conn, msgs))
    p2 = multiprocessing.Process(target=reciever, args=(child_conn,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
