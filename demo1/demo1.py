from tornado import gen
from tornado.httpclient import AsyncHTTPClient
from tornado.ioloop import IOLoop

# 使用异步客户端AsyncHTTPClient进行页面访问，装饰器@gen.coroutine声明这是一个协程函数。
# 使用yield关键字，代码中不用再编写灰调函数用于处理访问的结果，而可以在yield语句后面编写结果处理语句
@gen.coroutine
def coroutine_visit():
    http_client = AsyncHTTPClient()
    response = yield http_client.fetch('https://www.baidu.com')
    print(response.body)

# 由于tornado协程基于Python的关键字yield实现，所以不能像调用普通函数一样调用协程函数。
# 协程函数可以由以下三种方式调用
# 1、本身时协程的函数内通过yield关键字进行调用
@gen.coroutine
def outer_coroutine():
    print('start call another coroutine')
    yield coroutine_visit()
    print('stop of out_coroutine')

# 2、在IOLoop尚未启动时，通过IOLoop的run_sync()函数调用
# IOLoop是tornado的主事件循环对象，tornado程序通过他监听外部客户端的访问请求，并执行操作
def func_normal():
    print('start call another coroutine')
    IOLoop.current().run_sync(lambda: coroutine_visit())
    print('stop of out_coroutine')

# 3、在IOLoop已经启动时，通过IOLoop的spawn_callback()函数调用
# spawn_callback()函数不会等待被调用协程执行完成，所以spawn_callback()之前和之后的print会连续执行
# 而coroutine_visit本身将会由IOLoop在合适的时机调用
# spawn_callback()方法没有提供获取协程返回值的方法，所以只能调用没有返回值的协程函数
def func_normal2():
    print('start call another coroutine')
    IOLoop.current().spawn_callback(coroutine_visit)
    print('end')

