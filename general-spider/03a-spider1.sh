#!/bin/sh

. ../../venv/bin/activate
exec scrapy crawl general -L INFO -s FRONTERA_SETTINGS=frontier.spider_settings -s SEEDS_SOURCE=bikeaholics.txt -s SPIDER_PARTITION_ID=0
