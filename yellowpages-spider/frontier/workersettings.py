# -*- coding: utf-8 -*-
from frontera.settings.default_settings import MIDDLEWARES
from kafka_settings import *

MAX_NEXT_REQUESTS = 512
SPIDER_FEED_PARTITIONS = 2
SPIDER_LOG_PARTITIONS = 1

#--------------------------------------------------------
# Url storage
#--------------------------------------------------------

BACKEND = 'frontera.contrib.backends.sqlalchemy.SQLAlchemyBackend'
#BACKEND = 'frontera.contrib.backends.sqlalchemy.Distributed'

SQLALCHEMYBACKEND_ENGINE = 'postgresql://scrapy:scrapy@postgres.scrapy.quixey.com/yellowpages'

SQLALCHEMYBACKEND_ENGINE_ECHO = False
SQLALCHEMYBACKEND_DROP_ALL_TABLES = True
SQLALCHEMYBACKEND_CLEAR_CONTENT = True

from datetime import timedelta
SQLALCHEMYBACKEND_REVISIT_INTERVAL = timedelta(hours=1)


MIDDLEWARES.extend([
    'frontera.contrib.middlewares.domain.DomainMiddleware',
    'frontera.contrib.middlewares.fingerprint.DomainFingerprintMiddleware'
])

LOGGING_CONFIG='logging.conf'