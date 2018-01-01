"""
可以将配置信息以字典形式写在单独的py文件中
在初始化Application得时候作为第二个参数解包传递进去
字典中的信息都会被保存在Application对象的settings属性中 settings是一个字典

"""
from tornado.web import Application, RequestHandler
from tornado import httpserver
from tornado import ioloop
from day1_meet_tornado import config


class MyHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write("about_options")


if __name__ == '__main__':

    app = Application([
        (r'/', MyHandler),
    ], **config.args)

    print(app.settings.get('username'))
    server = httpserver.HTTPServer(app)
    server.bind(8000)
    ioloop.IOLoop.current().start()

