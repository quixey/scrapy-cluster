#!/bin/sh

. venv/bin/activate
cd crawler
exec scrapy runspider crawling/spiders/seatgeek_spider_example.py
