# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field
class SampleCrawler(Item):

    pid=Field()
    name=Field()
    category=Field()
    brand=Field()
    
    listprice=Field()
    salesprice=Field()
    avgrate=Field()
