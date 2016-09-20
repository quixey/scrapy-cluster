# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class AppItem(scrapy.Item):

    app_id = Field()
    name = Field()
    category = Field()
    download_url = Field()
    context = Field()
    content_source = Field()
    store_id = Field()
    date_published = Field()
    date_first_published = Field()
    icon_url = Field()
    app_version = Field()
    description = Field()
    os_requirements = Field()
    author = Field()
    locale = Field()
    ios_id = Field()

    ios_mt = Field()
    whatsnew = Field()
    size = Field()
    languages = Field()
    content_rating = Field()
    current_version_rating = Field()
    current_version_rating_count = Field()
    all_version_rating = Field()
    all_version_rating_count = Field()
    price = Field()
    currency = Field()
    screenshot_url = Field()
    reviews = Field()
    content_origin = Field()
    store_id = Field()
    currency = Field()
    ios_text_id = Field()
    provenance = Field()
    quixey_properties = Field()
    crawled = Field()
    created = Field()
    http_status_code = Field()

