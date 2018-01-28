from scrapy.crawler import CrawlerProcess

from sporttech_bots.spiders.paddypower_spider import \
    PaddypowerSpider
from sporttech_bots.spiders.skybet_spider import \
    SkybetSpider
from sporttech_bots.spiders.williamhill_spider import \
    WilliamhillSpider


class InfoVisualizer(object):

    def __init__(self):
        super(InfoVisualizer, self).__init__()

    def show_common_matrix(self):
        process = CrawlerProcess()
        process.crawl(PaddypowerSpider)
        process.crawl(SkybetSpider)
        process.crawl(WilliamhillSpider)
        process.start()
        print('Done')


if __name__ == '__main__':
    visualizer = InfoVisualizer()
    visualizer.show_common_matrix()
