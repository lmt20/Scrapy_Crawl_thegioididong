# -*- coding: utf-8 -*-
import scrapy
from ..items import BrandItem


class BrandsSpider(scrapy.Spider):
    name = 'brands'
    allowed_domains = ['thegioididong.com']
    start_urls = ['https://www.thegioididong.com/dtdd']

    def parse(self, response):
        brand = BrandItem()
        brand_nodes = response.css('.manu14 a')
        for brand_node in brand_nodes:
            if brand_node.css('img'):
                brand_id = brand_node.css('::attr(data-id)').get()
                brand_link = brand_node.css('::attr(href)').get()
                brand_name = brand_link[brand_link.find("-")+1:]
                brand['brand_id'] = brand_id
                brand['brand_name'] = brand_name
                yield brand
