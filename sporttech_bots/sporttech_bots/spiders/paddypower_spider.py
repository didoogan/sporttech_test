import scrapy

from helper.common import Common


class PaddypowerSpider(scrapy.Spider):
    name = Common.PADDYPOWER_SPIDER_NAME

    @staticmethod
    def parse_bet(bet, result):
        country = bet.xpath('child::*/text()')[0].extract()
        coefficient_fraction = bet.xpath('child::*/text()')[1].extract()
        numerator = coefficient_fraction.split('/')[0]
        denominator = coefficient_fraction.split('/')[1]
        result[country] = round(int(numerator) / int(denominator), 1)

    def start_requests(self):
        urls = [
            'http://www.paddypower.com/football/international-football/world-cup-2018?ev_oc_grp_ids=1828129'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        bets = response.xpath('//a[@class="fb-odds-button"]')
        result = {}
        for bet in bets:
            self.parse_bet(bet, result)
        return result
