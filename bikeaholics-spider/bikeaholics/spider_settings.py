# -*- coding: utf-8 -*-
from frontera.settings.default_settings import MIDDLEWARES
from kafka_settings import *

MAX_NEXT_REQUESTS = 256
DELAY_ON_EMPTY = 5.0

MIDDLEWARES.extend([
    'frontera.contrib.middlewares.domain.DomainMiddleware',
    'frontera.contrib.middlewares.fingerprint.DomainFingerprintMiddleware'
])

#--------------------------------------------------------
# Crawl frontier backend
#--------------------------------------------------------
BACKEND = 'frontera.contrib.backends.remote.messagebus.MessageBusBackend'
SPIDER_FEED_PARTITIONS = 2
