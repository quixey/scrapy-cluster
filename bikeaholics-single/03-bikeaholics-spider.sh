#!/bin/sh

. ../venv/bin/activate

# To enable page logging, add:
#   -s FEED_URI=bikeaholics.jsons -s FEED_FORMAT=jsonlines

exec scrapy crawl general -L INFO -s FRONTERA_SETTINGS=bikeaholics.spider_settings -s SEEDS_SOURCE=bikeaholics/bikeaholics.txt $@
