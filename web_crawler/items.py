from scrapy.item import Item, Field


class ImageItem(Item):
    img_url = Field()
    images = Field()
