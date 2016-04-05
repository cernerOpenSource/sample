# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field
class ReviewCrawler(Item):
    userid=Field()
    pid=Field()
    date=Field()
    helpful=Field()
    totalreview=Field()
    rating=Field()
    title=Field()
    rbody=Field()
    reviewid=Field()
    
    
