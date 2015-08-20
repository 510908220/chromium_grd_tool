__author__ = 'Administrator'
import os
import tornado.ioloop
import tornado.httpserver
import tornado.web
from handler.handler import *
from handler.conf import *
settings = dict(
            blog_title=u"Resource Tools",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
            debug=True,
        )
handlers = [
		(r"/",IndexHandler),

        (r"/add",Add),
        (r"/modify/(.*?)",Modify),
        (r"/history/",History),
		(r"/tool",Tool),
        (r"/help",Help),



]
application = tornado.web.Application(handlers, **settings)
if __name__ == "__main__":

	http_server = tornado.httpserver.HTTPServer(application)
	http_server.listen(PORT)
	tornado.ioloop.IOLoop.instance().start()
