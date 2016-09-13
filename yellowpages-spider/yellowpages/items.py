# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

def serialize_id(value):
    return '@%s' % str(value)

class YellowpagesItem(scrapy.Item):
    # define the fields for your item here like:
#    id = scrapy.Field(serializer=serialize_id)
    id = scrapy.Field()
    name = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    listingId = scrapy.Field()
    geo = scrapy.Field()
    #optional fields
    rating = scrapy.Field()
    description = scrapy.Field()
    telephone = scrapy.Field()
    category = scrapy.Field()
    ratingCount = scrapy.Field()
    concepts = scrapy.Field()
    address = scrapy.Field()
    crawled = scrapy.Field()
    created = scrapy.Field()
