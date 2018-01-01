"""
meet tornado
1.tornado  异步非阻塞io  核心ioloop  基于linux epoll 或BSD、MACOS kqueue实现
2.tornado 依赖操作系统 有平台限制
3.tornado 中的视图和Django视图函数不同,需要定义成视图类并继承tornado.web.RequestHandler
"""
from tornado.web import RequestHandler, Application
from tornado import ioloop


class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write("Hello Tornado!")


if __name__ == '__main__':
    app = Application([(r'/', IndexHandler)])
    app.listen(8099)
    ioloop.IOLoop.current().start()
