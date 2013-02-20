import tornado.ioloop
import tornado.web
import sys
import libvirt
import json
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        conn = libvirt.openReadOnly('qemu:///system')
        if conn == None:
            self.write('Failed to open connection to the hypervisor')
            return
        dict={}
        dict["hostname"]=conn.getHostname()
        dict["freememory"]=conn.getFreeMemory()
        dict["version"]=conn.getVersion()
        list=conn.listDefinedDomains()
        dict["domains"]=list
        dict["url"]=conn.getURI()
        dict["type"]=conn.getType()
        dict["info"]=conn.getInfo()
        dict["isAlive"]=conn.isAlive()
        dict["numOfDefinedDomains"]=conn.numOfDefinedDomains()
        dict["LibVersion"]=conn.getLibVersion()
        dict["interfaces"]=conn.listDefinedInterfaces()
        dict["networks"]=conn.listDefinedNetworks()
        dict["storagepools"]=conn.listDefinedStoragePools()
        ret=json.dumps(dict)
        self.write(ret)
        print ret
application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()