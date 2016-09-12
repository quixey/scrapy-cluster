# -*- coding: utf-8 -*-

# Scrapy settings for gplaycrawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'google_play_crawler_spider'

SPIDER_MODULES = ['google_play_crawler.spiders']
NEWSPIDER_MODULE = 'google_play_crawler.spiders'
CONCURRENT_REQUESTS_PER_DOMAIN = 100
ITEM_PIPELINES = {
		'google_play_crawler.pipelines.GplayPipeline': 300,
	}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Alo Ventures (+http://alo.ventures)'

REACTOR_THREADPOOL_MAXSIZE = 20
LOG_LEVEL = 'INFO'
COOKIES_ENABLED = False
##RETRY_ENABLED = False
DOWNLOAD_TIMEOUT = 60
##REDIRECT_ENABLED = False
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1

PROXY_LIST = './proxy/list.txt'
PROXY_USER_KEY='quixey2'
PROXY_USER_PASS='fg34gdsf85gdw'

#Proxy middelware
# Retry many times since proxies often fail
RETRY_TIMES = 10
# Retry on most error codes since proxies fail for different reasons
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]

DOWNLOADER_MIDDLEWARES = {
				'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware': 90,
			         # Fix path to this module
			        'google_play_crawler.spiders.randomproxy.RandomProxy': 100,
			        'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
			     }
