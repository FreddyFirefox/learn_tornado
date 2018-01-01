"""
global config argument   singleton options
"""
from tornado.options import options, parse_config_file, parse_command_line, define
from tornado.web import Application, RequestHandler
from tornado import httpserver
from tornado import ioloop


class MyHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write("about_options")


define(name="port", default=8000, type=int, help="this is a int number", multiple=False)

if __name__ == '__main__':
    # 接收命令行参数 如 python xx.py --port=8080
    parse_command_line()

    app = Application([
        (r'/', MyHandler),
    ])

    server = httpserver.HTTPServer(app)
    server.bind(options.port)
    ioloop.IOLoop.current().start()

