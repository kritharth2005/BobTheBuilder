# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BidScraperItem(scrapy.Item):
    title = scrapy.Field()
    expiration_date = scrapy.Field()
    publish_date = scrapy.Field()
    category = scrapy.Field()
    solicitation_type = scrapy.Field()
    issuing_agency = scrapy.Field()    
    url = scrapy.Field()
