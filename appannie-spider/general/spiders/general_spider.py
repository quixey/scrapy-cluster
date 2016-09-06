from scrapy.spiders.init import InitSpider
from scrapy.http import Request, FormRequest
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spiders import Rule
from scrapy.utils.spider import iterate_spider_output
from scrapy.selector import Selector

import scrapy
import randomproxy
import base64
import json

class AppAnnieSpider(InitSpider):
    name = 'appannie'
    allowed_domains = ['appannie.com']
    login_page = 'http://www.appannie.com/account/login'
    #start_urls = []#['http://www.appannie.com/apps/google-play/top-chart/united-states/overall']
    randomproxy = randomproxy.RandomProxy()



    def __init__(self, *args, **kwargs):
        #urlList = open('../configs/appannie/appAnnieUrls.txt')
        #for line in urlList.readlines():
        #    self.start_urls.append(line.replace('\n',''))

        super(AppAnnieSpider, self).__init__(*args, **kwargs)


    def init_request(self):
        """This function is called before crawling starts."""

        req = Request(url=self.login_page, callback=self.login)

        self.randomproxy.generateRandomProxy()
        req.meta['proxy'] = self.randomproxy.proxy_address
        basic_auth = 'Basic ' + base64.encodestring(self.randomproxy.user_pass)
        req.headers['Proxy-Authorization'] = basic_auth

        return req

    def login(self, response):
        """Generate a login request."""
        return FormRequest.from_response(response,
                    formdata={'username': 'qappany@quixey.com', 'password': 'quixey123'},
                    callback=self.check_login_response)

    def check_login_response(self, response):
        """Check the response returned by a login request to see if we are
        successfully logged in.
        """
        if "Quixey Appannie" in response.body:
            self.log("Successfully logged in. Let's start crawling!")
            # Now the crawling can begin..
            #self.initialized()
            #self.randomproxy.generateRandomProxy()
            #import pdb; pdb.setTrace()
            '''for i in range(0, len(self.start_urls)):
                req = scrapy.Request(url=self.start_urls[i])
                #req.headers = response.headers
                req.meta['proxy'] = self.randomproxy.proxy_address
                basic_auth = 'Basic ' + base64.encodestring(self.randomproxy.user_pass)
                req.headers['Proxy-Authorization'] = basic_auth
                yield req'''
            yield "SUCCESS"
        else:
            self.log("Bad times :(")
            yield "FAIL"
            # Something went wrong, we couldn't log in, so nothing happens.

    def parse(self, response):
        #import pdb; pdb.set_trace()
        # Scrape data from page
        if 'qappany@quixey.com' in response.body:
            chart = [[],[],[],[],[]]
            chartEmptyBoolean = [False, False, False, False, False]
            for i in range(1,101):
                row = Selector(response).xpath('//*[@id="storestats-top-table"]/tr[{}]'.format(str(i)))
                for j in range(1,6):
                    if chartEmptyBoolean[j-1]:
                        continue
                    elif 'td class="empty-cell"' in row.xpath('td[{}]'.format(str(j))).extract()[0]:
                        chartEmptyBoolean[j-1] = True
                        continue
                    else:
                        title = row.xpath('td[{}]/div/div[2]/span[1]/span[1]'.format(str(j))).extract()[0].split('title="')[1].split('"')[0]
                        title = self.formatAppAnnieTitle(title)
                        if (None is not title) or ('' != title):
                            chart[j-1].append(title)

            yieldChart = { "Top Free" : chart[0], "Top Paid" : chart[1], "Top Grossing" : chart[2], "Top New Free" : chart[3], "Top New Paid" : chart[4] }

            responseStatusString = str(response)
            chartName = 'chart'
            if 'united-states' in responseStatusString:
                chartName = 'United States'
            elif 'india' in responseStatusString:
                chartName = 'India'

            yield {str(chartName) : yieldChart}
        else:
            yield { 'body' : 'TEST'}


    def formatAppAnnieTitle(self, title):
        return title.replace('&amp;', '&')