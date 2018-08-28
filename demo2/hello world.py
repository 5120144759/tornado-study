import tornado.ioloop
import tornado.web

# 实现一个RequestHandler子类，重写get()方法，该函数负责get请求的处理
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        items = ['python', 'Java', 'C++']
        self.render('index/html', items=items)


# 定义一个make_app方法，返回一个web.Application对象，该对象的第一个参数用于定义tornado程序的路由映射，第二个参数为映射的函数
def make_app():
    return tornado.web.Application([
        (r'/', MainHandler),
    ])

# app.listen()指定了服务器的监听端口
def main():
    app = make_app()
    app.listen(8585)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()
