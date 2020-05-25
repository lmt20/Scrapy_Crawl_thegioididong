# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProductItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    brand_id = scrapy.Field()
    product_id = scrapy.Field()
    product_name = scrapy.Field()
    product_image = scrapy.Field()
    product_price = scrapy.Field()
    product_info = scrapy.Field()


class BrandItem(scrapy.Item):
    brand_id = scrapy.Field()
    brand_name = scrapy.Field()
