import scrapy

from helper.common import Common


class SkybetSpider(scrapy.Spider):
    name = Common.SKYBET_SPIDER_NAME

    @staticmethod
    def get_number(number):
        if ',' in number:
            return int(number.split(',')[0])
        return int(number)

    @classmethod
    def parse_substring(cls, substring, result):
        country = substring.split('name')[1].split('":"')[1].split('",')[0]
        num = substring.split('num')[1].split('":')[1].split(',')[0]
        den = substring.split('den')[1].split('":')[1].split('}')[0]
        num = cls.get_number(num)
        den = cls.get_number(den)
        result[country] = round(int(num) / int(den), 1)

    def start_requests(self):
        urls = [
            'https://m.skybet.com/football/world-cup-2018/event/16742642?DCMP=bet_responsivesiteredirect&expire_site_stick=1'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        result = {}
        substrings = str(response.body).split('isplayOrder')[2:]
        for substring in substrings:
            self.parse_substring(substring, result)
        Common.write_result(self.name, result)
