#!c:\Python27\python.exe
#!/usr/bin/env python
import cgi, cgitb 
form = cgi.FieldStorage()
file=open('name.txt','r')
for i in file:
    a=i
link = form.getvalue('link')
print "Content-Type: text/html"
print
print """
    <html>
    <head>
    <title>Spam Fighter</title>
    <link href='/style.css' rel='stylesheet' type='text/css' />
    </head>
    <body>
            <!--top part start -->
            <div id="top">
    <a href="/homepage.html"><img src='/spamlogo.jpg' alt='individual' width='286' height='66' border='0' /></a>
      <ul>
      <li class="hover">home</li>
      <li><a href="#">about us</a></li>
      <li><a href="#">contact us</a></li>
      </ul>
            </div>
            <!--top part end -->
            <!--header start -->
            <div id="header">
            <h2><span>Why Spam Fighter???</span></h2>
            <p>It has become a common practice for people to read online opinions/reviews for different purposes. For example, if one wants to buy a product, one typically goes to a review site (e.g., amazon.com) to read some reviews of the product. If most reviews are positive, one is likely to buy the product. If most reviews are negative, one will almost certainly not buy it. Positive opinions can result in significant financial gains and/or fames for busineses, organizations and individuals. This, unfortunately, gives strong incentives for opinion spamming.</p>
            </div>
            <!--header end -->
            <!--body start -->
            <div id="body" style="color:#000">
            <br class="spacer" style="color:#000" />
      <!--left panel start --><!--left panel end -->
       <!--mid panel start --><!--mid panel end -->
        <!--right panel start --><!--right panel end -->
            <!--bodyBottom start --><!--bodyBottom end-->
            <blockquote>
             <blockquote>
            <font color="#7642A3" size="+2"> <b>Hello """+a+"""</font></b></center><a href="/homepage.html" ><img src='/exit.jpg' align='right'></a>
<center>
        
         <center><b><font color="#7642A3">File downloaded successfully!!</font></b></center>
         <table width="200" border="0" cellpadding="25">
      <tr>
        <td><a href="/cgi-bin/display.py" ><img src=' /update1.png ' onmouseover="this.src=' /update2.jpg '" onmouseout="this.src=' /update1.png  '"  /></a></td>
      <td><a href="/cgi-bin/uploadfile.py" ><img src=' /file1.jpg ' onmouseover="this.src=' /file2.jpg '" onmouseout="this.src=' /file1.jpg  '"  /></a></td>
      <td><a href="/cgi-bin/uploadlink.py" ><img src=' /link1.jpg ' onmouseover="this.src=' /link2.jpg '" onmouseout="this.src=' /link1.jpg  '"  /></a></td>
      </tr>
     <tr><td>< a href="/newfeaturefile.py" ><font color="#7642A3">Fake users</font></a></td>
     <td>< a href="/reviewpolar.py" ><font color="#7642A3">Fake Reviews</font></a></td>
     </tr>
     
    </table>
     </center>
     <center>
      </blockquote>
     </blockquote>
    <br class="spacer" />
    <br class="spacer" />
    <br class="spacer" />
    <br class="spacer" />
    <br class="spacer" />
    
    <br class="spacer" />
            </div>
            <!--body end -->
            <!--footer start --><!--footer end -->
    </body>
    </html>
    
"""


from twisted.internet import reactor

from scrapy import log, signals
from scrapy.crawler import Crawler
from scrapy.settings import Settings
from scrapy.xlib.pydispatch import dispatcher
import logging
from reviewitem import ReviewCrawler
from scrapy.spider import Spider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
import urlparse
from items import  SampleCrawler
from reviewitem import ReviewCrawler
import csv
class MySpiderd(Spider):
    name = "saibaba123"
    allowed_domains=["flipkart.com"]
    start_urls=[link]
    
    def parse(self,response):
        cs = csv.writer(open("BAD.csv", "wb"))
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
        
        
        cs.writerow([item['pid'], item['name'],item['brand'],item['listprice'],item['salesprice'],item['avgrate']])
        
        name=hxs.select('//div[@class="fclear line bmargin10"]/a').extract()
        yield Request(urlparse.urljoin(response.url,name),self.par_ur)

        
    def par_ur(self,response):
         hxs=HtmlXPathSelector(response)
         #name=hxs.select('//a[@class="load-user-widget fk-underline"]')
         name=hxs.select('//div[@class="fclear line bmargin10"]/a')
         csk = csv.writer(open("BADREVIEW.csv", "wb"))


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
             csk.writerow([item['pid'][0], item['rating'][0],item['userid'][0],item['date'][0],item['title'][0],item['rbody'][0],item['helpful'],item['totalreview']])
             

         
         next_page=hxs.select('//a[@class="nav_bar_next_prev"]/@href').extract()       
         for n in next_page:
             if n:
                yield Request(urlparse.urljoin("http://www.flipkart.com",n),callback=self.par_ur)  
     
def stop_reactor():
    reactor.stop()

    

dispatcher.connect(stop_reactor, signal=signals.spider_closed)
spider = MySpiderd()
crawler = Crawler(Settings())
crawler.configure()
crawler.crawl(spider)
crawler.start()
log.start(loglevel=logging.DEBUG)
log.msg('Running reactor...')
reactor.run()  # the script will block here until the spider is closed
log.msg('Reactor stopped.')   
            



    
        
        
       
