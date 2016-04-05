#!c:\Python27\python.exe
#!/usr/bin/env python
  
import cgi
import cgitb; cgitb.enable()  # for troubleshooting

print "Content-type: text/html"
print 
print """ abc """

from twisted.internet import reactor

from scrapy import log, signals
from scrapy.crawler import Crawler
from scrapy.settings import Settings
from scrapy.xlib.pydispatch import dispatcher
import logging


from flipdet import MySpider1


def stop_reactor():
    reactor.stop()

    

dispatcher.connect(stop_reactor, signal=signals.spider_closed)
spider = MySpider1()
crawler = Crawler(Settings())
crawler.configure()
crawler.crawl(spider)
crawler.start()
log.start(loglevel=logging.DEBUG)
log.msg('Running reactor...')
reactor.run()  # the script will block here until the spider is closed
log.msg('Reactor stopped.')   
