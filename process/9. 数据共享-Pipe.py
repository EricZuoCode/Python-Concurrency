import multiprocessing

def sender(conn):
    conn.send("来自发送进程的消息")
    conn.close()

def receiver(conn):
    msg = conn.recv()
    print(f"收到消息: {msg}")
    conn.close()

if __name__ == "__main__":
    # Pipe 返回一对连接对象（双工管道），两端各持有一个
    conn_a, conn_b = multiprocessing.Pipe()
    p1 = multiprocessing.Process(target=sender, args=(conn_a,))
    p2 = multiprocessing.Process(target=receiver, args=(conn_b,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
