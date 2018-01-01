"""
use tornado httpserver bind port
"""
from tornado.web import Application, RequestHandler
from tornado import httpserver
from tornado import ioloop


class TestHandler(RequestHandler):
    """define a test handler"""

    def get(self, *args, **kwargs):
        """ override base class get method"""
        self.write("use tornado httpserver")


if __name__ == '__main__':
    # create a Application app with arguments urls
    app = Application([(r'/', TestHandler)])

    # 以app为参数，初始化一个tornado 服务器
    tornado_server = httpserver.HTTPServer(app)

    # 服务器绑定端口
    tornado_server.bind(8000)

    # 开启两个进程
    tornado_server.start(2)

    # 将创建的服务器socket 添加到epoll 开启监听 ioloop开启轮询
    ioloop.IOLoop.current().start()
