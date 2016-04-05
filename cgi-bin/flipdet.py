#!/usr/bin/env python
from scrapy.spider import Spider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
import urlparse
from items import  SampleCrawler
import csv
class MySpider1(Spider):
    name = "saibaba123"
    allowed_domains=["flipkart.com"]
    start_urls=["http://www.flipkart.com/laptop-accessories/usb-gadgets/pr?p%5B%5D=sort%3Dprice_asc&sid=6bo%2Cai3%2C0xm&ref=7112b8f8-e220-4cf0-85bd-d3eb52c05233"]
    
    def parse(self,response):
        c = csv.writer(open("OM.csv", "wb"))
        hxs=HtmlXPathSelector(response)
        id=[]
        prodid=hxs.select('//div[@class="product-unit unit-4"]')
        print prodid
        for pid in prodid:
            print pid.select('@data-pid').extract()
        produrl=hxs.select('//div[@class="pu-title fk-font-13"]/a/@href')
        for purl in produrl:
            y= purl.extract()
            id.append(y)    
        for s in id:
             yield Request(urlparse.urljoin("http://www.flipkart.com",s),meta={'csv':c},callback=self.parseprod)
             
            



    def parseprod(self, response):
        cs = response.meta['csv']
        hxs=HtmlXPathSelector(response)
        items=[]       
        item=SampleCrawler()
        name=hxs.select('//div[@class="mprod-summary-title fksk-mprod-summary-title"]/h1')
        item['pid']=hxs.select('//img/@data-pid').extract()
        item['name']=name.select('normalize-space(./text())').extract()
        item['avgrate']=hxs.select('//div[@class="pp-big-star"]/text()').extract()
        item['listprice']=hxs.select('//span[@class="price list old-price"]/text()').extract()
        item['salesprice']=hxs.select('//span[@class="fk-font-verybig pprice fk-bold"]/text()').extract()
        br=hxs.select('//table[@class="fk-specs-type2"]')
        brn=br[0].select('//td')
        
        #l=br.index('Brand')
        #item['brand']=br[l+1]
        #for i in brn:
        #    print i.select('./text()').extract()
                
        brand=brn.select('./text()').extract()
        n=brand.index('Brand')
        item['brand']=brand[n+1]
        items.append(item)
        
        
        cs.writerow([item['pid'][0], item['name'][0],item['brand'][0],item['listprice'][0],item['salesprice'][0],item['avgrate'][0]])
        return item
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
        
