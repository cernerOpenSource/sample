#!/usr/bin/env python
from scrapy.spider import Spider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
import urlparse
from reviewitem import ReviewCrawler
class MySpiderreview(Spider):
    name = "omsaibabareview"
    allowed_domains=["flipkart.com"]
    start_urls=["http://www.flipkart.com/laptop-accessories/usb-gadgets/pr?p%5B%5D=sort%3Dprice_asc&sid=6bo%2Cai3%2C0xm&ref=7112b8f8-e220-4cf0-85bd-d3eb52c05233"]
    
    def parse(self,response):
        hxs=HtmlXPathSelector(response)
        w=[]
        produrl=hxs.select('//div[@class="pu-title fk-font-13"]/a/@href')
        for purl in produrl:
            y= purl.extract()
            w.append(y)
        
        for s in w:
             link=urlparse.urljoin("http://www.flipkart.com",s)+"#readreviews"
             yield Request(urlparse.urljoin("http://www.flipkart.com",link),self.par_ur)

            

    def par_ur(self,response):
         hxs=HtmlXPathSelector(response)
         name=hxs.select('//a[@class="load-user-widget fk-underline"]')
         
         items=[]
         
         i=0;
         z=len(name)
         while(i<z):
             item=ReviewCrawler()
             revstar=hxs.select('//div[@class="fk-stars"]')
             item['pid']=hxs.select('//img/@data-pid').extract()
             item['rating']=revstar[i].select('normalize-space(@title)').extract()
             revname=hxs.select('//a[@class="load-user-widget fk-underline"]')
             item['userid']=revname[i].select('normalize-space(./text())').extract()
             revdate=hxs.select('//div[@class="date line fk-font-small"]')
             item['date']=revdate[i].select('normalize-space(./text())').extract()
             revoverview=hxs.select('//div[@class="line fk-font-normal bmargin5 dark-gray"]')
             item['title']=revoverview[i].select('normalize-space(strong/text())').extract()
             revreview=hxs.select('//p[@class="line bmargin10"]')
             item['rbody']=revreview[i].select('normalize-space(./text())').extract()
             helpful=hxs.select('//div[@class="unit"]/strong/text()')
             
             item['helpful']=helpful[0].extract()
             item['totalreview']=helpful[1].extract()
             
             
             items.append(item)
             i=i+1
             
             yield item

         
         next_page=hxs.select('//a[@class="nav_bar_next_prev"]/@href').extract()       
         for n in next_page:
             if n:
                yield Request(urlparse.urljoin("http://www.flipkart.com",n),callback=self.par_ur)  
