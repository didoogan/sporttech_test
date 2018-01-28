BOT_NAME = 'sporttech_bots'

SPIDER_MODULES = ['sporttech_bots.spiders']
NEWSPIDER_MODULE = 'sporttech_bots.spiders'

ROBOTSTXT_OBEY = True

# ITEM_PIPELINES = {
#    'sporttech_bots.pipelines.JsonWriterPipeline': 300,
# }

DOWNLOADER_MIDDLEWARES = {
    'sporttech_bots.middlewares.ProxyMiddleware': 1,
}