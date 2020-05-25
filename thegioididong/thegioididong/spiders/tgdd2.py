# # -*- coding: utf-8 -*-
# import scrapy
# import os
# from ..items import ThegioididongItem


# class TgddSpider(scrapy.Spider):
#     name = 'tgdd3'
#     allowed_domains = ['thegioididong.com']
#     origin_domain = 'https://www.thegioididong.com'
#     start_urls = ['https://www.thegioididong.com/dtdd']

#     def parse(self, response):
#         brands = response.css('.manu14 a')
#         for brand in brands:
#             if brand.css('img'):
#                 brand_link = TgddSpider.origin_domain + \
#                     brand.css('::attr(href)').get()
#                 # yield {"brand_link" : brand_link}
#                 yield response.follow(brand_link, callback=self.crawl_product)

#     def crawl_product(self, response):
#         products = response.css('.item')
#         for product in products:
#             product_id = product.css('::attr(data-productid)').get()
#             product_name = product.css('h3::text').get()
#             if product.css('img::attr(data-original)'):
#                 product_image = product.css('img::attr(data-original)').get()
#             else:
#                 product_image = product.css('img::attr(src)').get()
#             product_price = product.css('.price strong::text').get()
#             product_link = self.origin_domain + \
#                 product.css('a::attr(href)').get()

#             # product_info = response.follow(
#             #     product_link, callback=self.crawl_info)
#             #     brand_link, callback=self.crawl_product)
#             item = ThegioididongItem()
#             item['product_id'] = product_id
#             item['product_name'] = product_name
#             item['product_image'] = product_image
#             item['product_price'] = product_price

#             # yield {"product_id": product_id, "product_name": product_name,
#             #        "product_image": product_image, "product_price": product_price,
#             #        "product_info": product_info}
#             yield scrapy.Request(
#                 product_link, callback=self.crawl_info, meta={'item': item})

#     def crawl_info(self, response):
#         item = response.meta['item']

#         total_infor = ""
#         infors = response.css('.parameter li')
#         for infor in infors:
#             infor_content_list = infor.css('::text').getall()
#             infor_content = " ".join(infor_content_list)
#             total_infor += infor_content + "\n"

#         article = " ".join(response.css(
#             '.area_article > :not([class="boxRtAtc"])').css('::text').getall())
#         item["product_info"] = total_infor + article
#         yield item
