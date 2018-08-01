# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SlashdotItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    description = scrapy.Field()
    story_byline = scrapy.Field()
    title = scrapy.Field()
