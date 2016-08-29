#!/bin/sh

. ../venv/bin/activate
exec scrapy crawl general -L INFO -s FRONTERA_SETTINGS=bikeaholics.spider_settings
