import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
import urllib.parse


class FlagImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in item['img_url']:
            yield scrapy.Request("https:" + image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item

    def file_path(self, request, response=None, info=None, *, item=None):
        image_perspective = request.url.split('/')[-2]
        image_filename = f'{urllib.parse.unquote(image_perspective)}.jpg'

        return image_filename
