BOT_NAME = 'web_crawler'

SPIDER_MODULES = ['web_crawler.spiders']
NEWSPIDER_MODULE = 'web_crawler.spiders'

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
   'web_crawler.pipelines.FlagImagesPipeline': 1
}
IMAGES_STORE = 'flags'

REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
