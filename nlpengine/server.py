import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import main as nlpengine
import sys
import json


from tornado.options import define, options
from google import google

define("port", default=8081, help="run on the given port", type=int)

class MainHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        print "setting headers!!!"
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
    def getQuepy(self):
        return nlpengine.ask(self.get_argument("question"))
    def getGoogle(self):
        search_results = google.search(self.get_argument("question"), 2)
        returnedObj = []
        for result in search_results:
            obj = {}
            obj['title'] = result.name
            obj['link'] = result.link
            obj['description'] = result.description
            returnedObj.append(obj)
        return returnedObj
    def get(self):
        data = {}
        data['quepyResults'] = self.getQuepy()  
        data['googleResults'] = self.getGoogle()
        self.write(data)


def main():
    tornado.options.parse_command_line()
    sys.path.append('/Users/work/Desktop/Veritas/nlpengine/nltk')
    application = tornado.web.Application([(r"/", MainHandler)])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    print("Server initialized on port " + str(options.port) + ".")
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
