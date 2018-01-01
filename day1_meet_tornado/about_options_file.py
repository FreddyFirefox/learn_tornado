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


# 向options中添加参数 如果没有添加 则在命令行或者配置文件中无法使用
define(name="port", default=8000, type=int, help="this is a int number", multiple=False)

if __name__ == '__main__':
    # 接收命令行参数 如 python xx.py --port=8080
    # parse_command_line()

    # 从配置文件中读取配置参数 参数需符合python语法 不支持字典类型数据
    parse_config_file('./config')

    app = Application([
        (r'/', MyHandler),
    ])

    server = httpserver.HTTPServer(app)
    server.bind(options.port)
    ioloop.IOLoop.current().start()

