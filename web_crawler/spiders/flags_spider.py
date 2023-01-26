import scrapy
from web_crawler.items import ImageItem


class FlagsSpider(scrapy.Spider):
    name = "flags"

    def start_requests(self):
        urls = ['https://en.wikipedia.org/wiki/Gallery_of_sovereign_state_flags']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for elem in response.xpath('//*[@id="mw-content-text"]/div[1]/ul[has-class("gallery mw-gallery-traditional")]/li[has-class("gallerybox")]/div/div[1]/div/a'):
            img_url = elem.xpath('img/@src').extract_first()
            yield {'img_url': [img_url]}
