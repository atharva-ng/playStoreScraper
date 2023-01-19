import scrapy
from ..items import PlaystorespiderItem
import requests



class PlaystorespiderSpider(scrapy.Spider):
    name = 'PlayStoreSpider'
    allowed_domains = ['play.google.com']
    start_urls = ['http://play.google.com/']

    def parse(self, response):
        itemLink = PlaystorespiderItem()
        links=response.css("a.Si6A0c::attr(href)").getall()

        linksf = []
        for str in links:
            linksf.append(str[23:])
        itemLink["link"]=linksf

        yield {"linksf":linksf}

