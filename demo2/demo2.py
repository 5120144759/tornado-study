import tornado.web
import tornado.httpclient
import tornado.ioloop

class MainHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        http = tornado.httpclient.AsyncHTTPClient()
        http.fetch('https://www.baidu.com', callback=self.on_response)

    def on_response(self, response):
        if response.error:
            raise tornado.web.HTTPError(500)
        self.write(response.body)
        self.finish()

def make_app():
    return tornado.web.Application([
        (r'/', MainHandler),
    ])

def main():
    app = make_app()
    app.listen(9598)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()