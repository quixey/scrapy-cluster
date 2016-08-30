# -*- coding: utf-8 -*-
from frontera.settings.default_settings import MIDDLEWARES

MAX_NEXT_REQUESTS = 256
DELAY_ON_EMPTY = 5.0

MIDDLEWARES.extend([
    'frontera.contrib.middlewares.domain.DomainMiddleware',
    'frontera.contrib.middlewares.fingerprint.DomainFingerprintMiddleware'
])

#--------------------------------------------------------
# Crawl frontier backend
#--------------------------------------------------------

# BACKEND = 'frontera.contrib.backends.remote.messagebus.MessageBusBackend'
# SPIDER_FEED_PARTITIONS = 2

BACKEND = 'frontera.contrib.backends.sqlalchemy.revisiting.Backend'

SQLALCHEMYBACKEND_ENGINE = 'postgresql://scrapy:scrapy@postgres.scrapy.quixey.com/bikeaholics'

SQLALCHEMYBACKEND_ENGINE_ECHO = False
SQLALCHEMYBACKEND_DROP_ALL_TABLES = True
SQLALCHEMYBACKEND_CLEAR_CONTENT = True
from datetime import timedelta
SQLALCHEMYBACKEND_REVISIT_INTERVAL = timedelta(hours=1)

LOGGING_CONFIG='logging.conf'
