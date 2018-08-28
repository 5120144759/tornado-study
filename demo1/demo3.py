# 在协程中等待多个异步调用

from tornado import gen
from tornado.httpclient import AsyncHTTPClient
from tornado.ioloop import IOLoop

@gen.coroutine
def coroutine_list():
    http_client = AsyncHTTPClient()
    list_response = yield [http_client.fetch('https://www.baidu.com'),
                           http_client.fetch('https://www.sina.com'),
                           http_client.fetch('https://www.bilibili.com'),
                           http_client.fetch('https://www.douyu.com'),]
    for response in list_response:
        print(response.body)

@gen.coroutine
def coroutine_dict():
    http_client = AsyncHTTPClient()
    dict_response = yield { 'baidu': http_client.fetch('https://www.baidu.com'),
                            'sina': http_client.fetch('https://www.dina.com'),
                            'bilibili': http_client.fetch('https://www.bilibili.com'),
                            'douyu': http_client.fetch('https://www.douyu.com')
    }

    print(dict_response['baidu'].body)

@gen.coroutine
def func_normal():
    print('start')
    yield coroutine_dict()
    print('end')

func_normal()