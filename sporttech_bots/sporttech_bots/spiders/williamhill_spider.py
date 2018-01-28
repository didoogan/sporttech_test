import scrapy

from helper.common import Common


class WilliamhillSpider(scrapy.Spider):
    name = Common.WILLIAM_HILL_SPIDER_NAME

    @staticmethod
    def process_raw_country(raw_country):
        return raw_country.extract().strip()

    @staticmethod
    def process_raw_bet(raw_bet):
        result = raw_bet.extract().strip()
        numerator = result.split('/')[0]
        denominator = result.split('/')[1]
        return round(int(numerator) / int(denominator), 1)

    def start_requests(self):
        urls = [
            'http://sports.williamhill.com/bet/en-gb/betting/e/12085242/World+Cup+2018+-+Outright.html',

        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        raw_countries = response.xpath('//div[@class="eventselection"]/text()')
        countries = [self.process_raw_country(rc) for rc in raw_countries]
        raw_bets = response.xpath('//div[@class="eventprice"]/text()')
        bets = [self.process_raw_bet(rb) for rb in raw_bets]
        return dict(zip(countries, bets))
