import scrapy

from scrapy.http import Request
from lxmlhtml import CustomLxmlLinkExtractor as LinkExtractor
from scrapy.conf import settings

from crawling.items import RawResponseItem
from redis_spider import RedisSpider


class SeatGeekSpider(RedisSpider):
    '''
    A spider that walks all links from the requested URL. This is
    the entrypoint for generic crawling.
    '''
    name = "sg"

    def __init__(self, *args, **kwargs):
        super(SeatGeekSpider, self).__init__(*args, **kwargs)



    def parse(self, response):
        selectorList = response.css('.cell-wrapper a')
        selectListLength = len(selectorList)
        yield {
            'html body' : response.body
        }
        for i in range(0, selectListLength):
            yield{
                'name' : str(response.css('.cell-wrapper a')[i].extract().split('>')[1].replace('</a',''))
            }

'''   def start_requests(self):
        req = scrapy.Request(url=self.start_urls[0])

        self.randomproxy.generateRandomProxy()
        req.meta['proxy'] = self.randomproxy.proxy_address
        basic_auth = 'Basic ' + base64.encodestring(self.randomproxy.user_pass)
        req.headers['Proxy-Authorization'] = basic_auth


        yield req'''
