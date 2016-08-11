#!/bin/sh

. venv/bin/activate
cd crawler
exec scrapy runspider crawling/spiders/link_spider.py

