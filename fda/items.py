# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class FdaItem(Item):
    # define the fields for your item here like:
    url = Field()
    name = Field()
    name_first = Field()
    name_last = Field()
    name_middle = Field()
    eff_date = Field()
    debarment = Field()
    fr_date   = Field()
    volume_page = Field()
    time_stamp = Field()
