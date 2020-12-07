# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ParserWildUrl(scrapy.Item):
    url = scrapy.Field()
    unique_number = scrapy.Field()
    sections = scrapy.Field()


class ParserWildItem(scrapy.Item):
    timestamp = scrapy.Field()
    RPC = scrapy.Field()
    URL = scrapy.Field()
    title = scrapy.Field()
    marketing_tags = scrapy.Field()
    brand = scrapy.Field()
    section = scrapy.Field()
    price_data = scrapy.Field()
    stock = scrapy.Field()
    assets = scrapy.Field()
    metadata = scrapy.Field()
    variants = scrapy.Field()
