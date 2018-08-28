# 在协程中调用阻塞函数
# 在协程中直接调用阻塞函数会影响协程本身的性能，所以tornado提供了在协程中利用线程池调度阻塞函数
from tornado import gen
from concurrent.futures import ThreadPoolExecutor
import time

thread_pool = ThreadPoolExecutor(2)

def mySleep(count):
    for i in range(count):
        time.sleep(1)
        print(i)


@gen.coroutine
def call_blocking(): 
    print('start')
    yield thread_pool.submit(mySleep, 10)
    print(end)

call_blocking()