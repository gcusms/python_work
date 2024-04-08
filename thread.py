import threading
import time
from queue import Queue

def job(list_1,q):
    for i in range(len(list_1)):
        list_1[i] = list_1[i]**2
    q.put(list_1)


def multithreading(data):
    q = Queue()
    threads = []
    for i in range(len(data)):
        t = threading.Thread(target = job,args=(data[i],q))
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join

    results = []
    for _ in range(len(data)):
        results.append(q.get())
    print('results',results)



if __name__ == '__main__':
    data = [[1,2,3,4,5,6,7,8,9,0,1],[5,3,3]]
    
    multithreading(data)
    print('Main Threading Start')
