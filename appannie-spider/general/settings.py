# -*- coding: utf-8 -*-

# Scrapy settings for topic project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
from scrapy.settings.default_settings import SPIDER_MIDDLEWARES, DOWNLOADER_MIDDLEWARES

BOT_NAME = 'general'

SPIDER_MODULES = ['general.spiders']
NEWSPIDER_MODULE = 'general.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'topic (+http://www.yourdomain.com)'

SPIDER_MIDDLEWARES.update({
    'frontera.contrib.scrapy.middlewares.schedulers.SchedulerSpiderMiddleware': 1000,
    'scrapy.spidermiddleware.depth.DepthMiddleware': None,
    'scrapy.spidermiddleware.offsite.OffsiteMiddleware': None,
    'scrapy.spidermiddleware.referer.RefererMiddleware': None,
    'scrapy.spidermiddleware.urllength.UrlLengthMiddleware': None
})

DOWNLOADER_MIDDLEWARES.update({
    'frontera.contrib.scrapy.middlewares.schedulers.SchedulerDownloaderMiddleware': 1000,
    'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware' : 1,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 1
    })

SCHEDULER = 'frontera.contrib.scrapy.schedulers.frontier.FronteraScheduler'
SPIDER_MIDDLEWARES.update({
    'frontera.contrib.scrapy.middlewares.seeds.file.FileSeedLoader': 1,
})


HTTPCACHE_ENABLED = False
REDIRECT_ENABLED = True
COOKIES_ENABLED = True
COOKIES_DEBUG = True
DOWNLOAD_TIMEOUT = 240
RETRY_ENABLED = False
DOWNLOAD_MAXSIZE = 1*1024*1024

# auto throttling
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_DEBUG = False
AUTOTHROTTLE_MAX_DELAY = 3.0
AUTOTHROTTLE_START_DELAY = 0.25
RANDOMIZE_DOWNLOAD_DELAY = False

# concurrency
CONCURRENT_REQUESTS = 64
CONCURRENT_REQUESTS_PER_DOMAIN = 10
DOWNLOAD_DELAY = 0.0

LOG_LEVEL = 'INFO'

REACTOR_THREADPOOL_MAXSIZE = 32
DNS_TIMEOUT = 180
