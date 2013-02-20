import tornado.ioloop
import tornado.web
import libvirtvm
import sys
import libvirt
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        conn = libvirt.openReadOnly('qemu:///system')
        if conn == None:
            print 'Failed to open connection to the hypervisor'
            sys.exit(1)
        for id in conn.listDefinedDomains():
            self.write(id)
application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()