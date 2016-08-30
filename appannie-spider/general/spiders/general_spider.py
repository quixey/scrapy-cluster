import scrapy
import base64
import re
import random
import randomproxy
from scrapy.selector import Selector
import json


class AppAnnieSpider(scrapy.Spider):
    name = 'appannie'
    #start_urls = []#= ['http://seatgeek.com/concert-tickets/hip-hop']
    randomproxy = randomproxy.RandomProxy()

    def __init__(self, *args, **kwargs):
        super(AppAnnieSpider, self).__init__(*args, **kwargs)
        #urlList = open('../configs/appannie/appAnnieUrls.txt')
        #for line in urlList.readlines():
         #   self.start_urls.append(line.replace('\n',''))

    def parse(self, response):
        selectorListFree = Selector(response).xpath('//*[@id="free"]/div').css('span.product-name').extract()
        selectorListPaid = Selector(response).xpath('//*[@id="paid"]/div').css('span.product-name').extract()
        selectorListGrossing = Selector(response).xpath('//*[@id="grossing"]/div').css('span.product-name').extract()


        yield {
            'html body' : response.body
        }

        def extract_title(selectorList, i):
            return selectorList[i].split('title="')[1].split('"')[0]

        topFree = [ extract_title(selectorListFree, i) for i in range(len(selectorListFree))]
        topPaid = [ extract_title(selectorListPaid, i) for i in range(len(selectorListFree))]
        topGrossing = [ extract_title(selectorListGrossing, i) for i in range(len(selectorListFree))]

        #import pdb; pdb.set_trace()
        #//DIV[@id='free']/DIV[@class='list']/DIV[@class='item']/A/SPAN[@class='product-name']
        yield {'topFree' : topFree,
               'topPaid' : topPaid,
               'topGrossing' : topGrossing}

    def start_requests(self):
        req = scrapy.Request(url=self.start_urls[0])
        
        self.randomproxy.generateRandomProxy()
        req.meta['proxy'] = self.randomproxy.proxy_address
        basic_auth = 'Basic ' + base64.encodestring(self.randomproxy.user_pass)
        req.headers['Proxy-Authorization'] = basic_auth

        yield req