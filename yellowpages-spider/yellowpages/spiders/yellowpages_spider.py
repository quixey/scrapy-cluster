import scrapy
from scrapy.utils.sitemap import Sitemap
from scrapy.http import Request
import json
import string
from datetime import datetime
from yellowpages.items import YellowpagesItem
from scrapy.loader import ItemLoader
from scrapy.contrib.loader.processor import TakeFirst

class YellowPagesSpider(scrapy.Spider):
    name = "yellowpages"
#    start_urls = (
#        'http://webyp-sitemap.yellowpages.com/sitemaps/sitemap_index.xml',
#    )

    api_url = "http://pubapi.yp.com/search-api/search/devapi/details?listingid=$businessId&key=gn4scfy3gm&format=json"

    def parse2(self, response):
        businessId = '478610722'
        data_url = string.Template(self.api_url).substitute({'businessId': businessId})
        yield Request(data_url,self.parse_api_response)

    def parse(self, response):
        s = Sitemap(response.body)
        mip_list = []
        if s.type == 'sitemapindex':
            for sitelink in s:
                url = sitelink['loc']
#                if "/mip_" in url:
                if "/mip_000700_0_20160821" in url:
#                    print "Top-url %s mod  " % url,sitelink['lastmod']
                    mip_list.append(url) 
#                    yield Request(url,self.parse_mip,dont_filter=True)

        for url in mip_list:
            yield Request(url,self.parse_mip,dont_filter=True)

    def parse_mip(self, response):
#        print "Request url ",response.request.url
        s2 = Sitemap(response.body)
        biz_list = []
        if s2.type == 'urlset':
            for sitelink in s2:
                url2 = sitelink['loc'] 
#                if "/mip/" in url2:
                if "/mip/priest-nicole-l-md-478610722" in url2:
                    idx = url2.rfind('-')
                    if idx > 0:
                        businessId = url2[idx+1:]
                        biz_list.append(businessId)
#                        print "inside-url %s mod  " % url2,sitelink['lastmod']
                        data_url = string.Template(self.api_url).substitute({'businessId': businessId})
#                        print "sending api request ", data_url
                        timeIdx = sitelink['lastmod'].rfind(':00+00:00')

                        if timeIdx > 0:
                            lastmod = sitelink['lastmod'][:timeIdx] +'Z'

                        data_url = 'http://pubapi.yp.com/search-api/search/devapi/details?listingid=478610722&key=gn4scfy3gm&format=json'
                        yield Request(data_url,self.parse_api_response, meta={'lastmod':lastmod})
#        for businessId in biz_list:
#            data_url = string.Template(self.api_url).substitute({'businessId': businessId})
#            print "sending api request ", data_url
#            yield Request(data_url,self.parse_api_response)
    
    def parse_api_response(self, response):
        print "api response ",  response.request.url
        l = ItemLoader(item=YellowpagesItem())
        l.default_output_processor = TakeFirst()
        jsonresponse = json.loads(response.body_as_unicode())
        resultCode = jsonresponse['listingsDetailsResult']['metaProperties']['resultCode']
        details = jsonresponse['listingsDetailsResult']['listingsDetails']['listingDetail'][0]

        l.add_value('id', details['attribution'])
        l.add_value('name', details['businessName'])
        geo = {}
        geo['latitude'] = details['latitude']
        geo['longitude'] = details['longitude']
        l.add_value('geo',geo)
#        l.add_value('latitude', details['latitude'])
 #       l.add_value('longitude', details['longitude'])
        l.add_value('listingId', details['listingId'])
        #optional fields
        l.add_value('rating', details['averageRating'])
        l.add_value('description', details['generalInfo'])
        l.add_value('telephone', details['phone'])
        l.add_value('category', details['primaryCategory'])
        l.add_value('ratingCount', details['ratingCount'])
        addr = ','.join([details['street'],details['city'],details['state'],str(details['zip'])])
        l.add_value('address', addr)
        ts = datetime.utcnow().replace(microsecond=0).isoformat() +'Z'
        l.add_value('crawled', ts)
        l.add_value('created', response.meta['lastmod'])
        return l.load_item()

    def parse_api_response2(self, response):
#        print "api response ",  response.request.url
        item = YellowpagesItem()
        jsonresponse = json.loads(response.body_as_unicode())
        resultCode = jsonresponse['listingsDetailsResult']['metaProperties']['resultCode']
#        print "resultCode ",resultCode
        details = jsonresponse['listingsDetailsResult']['listingsDetails']['listingDetail'][0]

#        if hasattr(details, 'attribution'):
        item['id'] = details['attribution']
#        if hasattr(details, 'businessName'):
        item['name'] = details['businessName']
#        if hasattr(details, 'latitude'):
        item['latitude'] = details['latitude']
#        if hasattr(details, 'longitude'):
        item['longitude'] = details['longitude']
#        if hasattr(details, 'listingId'):
        item['listingId'] = details['listingId']
        #optional fields
#        if hasattr(details, 'averageRating'):
        item['rating'] = details['averageRating']
#        if hasattr(details, 'generalInfo'):
        item['description'] = details['generalInfo']
#        if hasattr(details, 'phone'):
        item['telephone'] = details['phone']
#        if hasattr(details, 'primaryCategory'):
        item['category'] = details['primaryCategory']
#        if hasattr(details, 'ratingCount'):
        item['ratingCount'] = details['ratingCount']
#        item['concepts'] = details['akas']['aka']
        addr = ','.join([details['street'],details['city'],details['state'],str(details['zip'])])
        item['address'] = addr
#    d = date.now()
        ts = datetime.utcnow().replace(microsecond=0).isoformat() +'Z'
        item['crawled'] = ts
        item['created'] = response.meta['lastmod']
#        print item
        yield item

    
