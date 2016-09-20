# -*- coding: utf-8 -*-

# Scrapy settings for topic project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
from scrapy.settings.default_settings import SPIDER_MIDDLEWARES, DOWNLOADER_MIDDLEWARES

BOT_NAME = 'apple'

SPIDER_MODULES = ['apple.spiders']
NEWSPIDER_MODULE = 'apple.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'topic (+http://www.yourdomain.com)'
USER_AGENT = "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Proxy middleware
# Retry many times since proxies often fail
RETRY_TIMES = 10
# Retry on most error codes since proxies fail for different reasons
RETRY_HTTP_CODES = [500, 503, 504, 400, 404, 408]

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.retry.RetryMiddleware' : 90,
    'apple.spiders.randomproxy.RandomProxy' : 100,
    'apple.spiders.robots_txt_middleware.robots_txt_middleware' : 110,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware' : 110,
    'scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware' : None,
}

SPIDER_MIDDLEWARES.update({
    'frontera.contrib.scrapy.middlewares.schedulers.SchedulerSpiderMiddleware': 1000,
    'scrapy.spidermiddleware.depth.DepthMiddleware': None,
    'scrapy.spidermiddleware.offsite.OffsiteMiddleware': None,
    'scrapy.spidermiddleware.referer.RefererMiddleware': None,
    'scrapy.spidermiddleware.urllength.UrlLengthMiddleware': None
})

DOWNLOADER_MIDDLEWARES.update({
    'frontera.contrib.scrapy.middlewares.schedulers.SchedulerDownloaderMiddleware': 1000,
    })

SCHEDULER = 'frontera.contrib.scrapy.schedulers.frontier.FronteraScheduler'
SPIDER_MIDDLEWARES.update({
    'frontera.contrib.scrapy.middlewares.seeds.file.FileSeedLoader': 1,
})


# Proxy list 
PROXY_LIST = './proxy/list.txt'
PROXY_USER_KEY = 'quixey2'
PROXY_USER_PASS = 'fg34gdsf85gdw'

HTTPCACHE_ENABLED = False
REDIRECT_ENABLED = True
COOKIES_ENABLED = False
DOWNLOAD_TIMEOUT = 240
RETRY_ENABLED = False
DOWNLOAD_MAXSIZE = 1*1024*1024

# auto throttling
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_DEBUG = True
AUTOTHROTTLE_MAX_DELAY = 60
AUTOTHROTTLE_START_DELAY = 5
RANDOMIZE_DOWNLOAD_DELAY = False
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0

# concurrency
CONCURRENT_REQUESTS = 64
CONCURRENT_REQUESTS_PER_DOMAIN = 10
DOWNLOAD_DELAY = 0.5

LOG_LEVEL = 'DEBUG'

REACTOR_THREADPOOL_MAXSIZE = 32
DNS_TIMEOUT = 180
