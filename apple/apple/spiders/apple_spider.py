
import scrapy
import time
import logging
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor

from apple.items import AppItem

class AppleSpider(scrapy.Spider):

    name = "apple"
    allowed_domains = ["apple.com"]
    start_urls = ["https://itunes.apple.com/us/genre/ios/id36?mt=8/"]
    obey_robotstxt = True


    def parse(self, response):

        print 'IN PARSE'

        # Get all the genres
	genres = response.selector.xpath('//div[@id="genre-nav"]')

        for genre in genres:
            # URL for each genre
            genre_page_links = response.xpath('//a[@class="top-level-genre"]/@href').extract()

            # For each genre, the apps are sorted by names and grouped under the correponding alphabet.
            for link in genre_page_links:
                request = scrapy.Request(link, callback=self.parse_alphabets)
    #B    request = scrapy.Request("https://itunes.apple.com/us/genre/ios-lifestyle/id6012?mt=8", callback=self.parse_alphabets)
                yield request


    def parse_alphabets(self, response):
        
        print 'IN ALPHABETS'

        # Get all the urls for each alphabet in this genre
        alphabets = response.xpath('//ul[@class="list alpha"]/li/a/@href').extract()

        # For each of the alphabetic group, get the apps
        for link in alphabets:
            print 'QDEBUG: ' + link
            request = scrapy.Request(link, callback=self.parse_app_list)
#b        request = scrapy.Request("https://itunes.apple.com/us/genre/ios-lifestyle/id6012?mt=8&letter=J", callback=self.parse_app_list)
            yield request


    def parse_app_list(self, response):

        print 'IN APP LIST'

        # Get all the apps on this page 
        apps = response.xpath('//div[@id="selectedcontent"]/div/ul/li/a/@href').extract()
        for link in apps:
            print 'QDEBUG: ' + link
            request = scrapy.Request(link, callback=self.parse_each_app)
            yield request

        # See if there is a next page, and if yes keep going until we are done with the pages for this alphabet
        next_page = response.selector.xpath('//ul[@class="list paginate"]/li/a[@class="paginate-more"]/@href').extract()
        if not not next_page:
            print 'QDEBUG: ' + next_page[0]
            yield scrapy.Request(next_page[0], self.parse_app_list)
        else:
            pages = response.selector.xpath('//ul[@class="list paginate"]/li/a/@href').extract()
            for page in pages:
                print 'QDEBUG: ' + page
                yield scrapy.Request(page, self.parse_app_list)

#B          yield scrapy.Request("https://itunes.apple.com/us/app/kindle-read-books-ebooks-magazines/id302584613?mt=8", self.parse_each_app)
#B          yield scrapy.Request("https://itunes.apple.com/us/app/jinnyboytv/id1041203205?mt=8", self.parse_each_app)
#B          yield scrapy.Request("https://itunes.apple.com/us/app/98.6-fever-watch/id999337846?mt=8", self.parse_each_app)
#B          yield scrapy.Request("https://itunes.apple.com/us/app/9-mesacev/id648300132?mt=8", self.parse_each_app)
#B          yield scrapy.Request("https://itunes.apple.com/us/app/9-minute-mommy-baby-workout/id918109778?mt=8", self.parse_each_app)
#B          yield scrapy.Request("https://itunes.apple.com/us/app/8th-wcpm-2014-mexico/id908953439?mt=8", self.parse_each_app)
#B          yield scrapy.Request("https://itunes.apple.com/us/app/7emes-assises-genetique-humaine/id803306236?mt=8", self.parse_each_app)
#B        yield scrapy.Request("https://itunes.apple.com/us/app/7-minute-workout-for-iphone/id990977210?mt=8", self.parse_each_app)
#B          yield scrapy.Request("https://itunes.apple.com/us/app/7-cups-anxiety-stress-depression/id921814681?mt=8", self.parse_each_app)
#B          yield scrapy.Request("https://itunes.apple.com/us/app/50-grey-areas-full/id1004321740?mt=8", self.parse_each_app)
#B          yield scrapy.Request("https://itunes.apple.com/us/app/5-terre-vocal-app/id813604998?mt=8", self.parse_each_app)
#B          yield scrapy.Request("https://itunes.apple.com/us/app/5-generations-one-port/id628083063?mt=8", self.parse_each_app)




    def parse_each_app(self, response):

        # Get the info for the app
        item = AppItem()
        app = response.selector.xpath('//div[@id="content"]')
        item['name'] = app.xpath('.//h1[@itemprop="name"]/text()').extract()        
        print item['name']

        item['category'] = app.xpath('.//span[@itemprop="applicationCategory"]/text()').extract()

#BC        item['description'] = app.xpath('.//p[@itemprop="description"]/text()').extract()
#BC        item['author'] = app.xpath('.//span[@itemprop="author"]/span[@itemprop="name"]/text()').extract()

#BC        item['app_version'] = app.xpath('//span[@itemprop="softwareVersion"]/text()').extract()
#BC        item['download_url'] = app.xpath('.//div[@class="lockup product application"]/a/@href').extract()
#BC        item['os_requirements'] = app.xpath('.//span[@itemprop="operatingSystem"]/text()').extract()

#BC        item['price'] = app.xpath('.//div[@class="price"]/text()').extract()
#BC        item['locale'] = "en_US"
#BC        item['currency'] = "USD"

#BC        item['content_source'] = "apple.com"
#BC        item['store_id'] = "itunes"

#BC        item['context'] = "http://schemas.quixey.com/2015/02/us-direct/appStores/itunes/context.jsonld"

#BC     NEED TO ADD THE REST OF THE FIELDS

        yield item
