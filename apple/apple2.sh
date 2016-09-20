#!/bin/sh

. ../venv/bin/activate
exec scrapy crawl apple -L INFO -s FRONTERA_SETTINGS=frontier.spider_settings -s SPIDER_PARTITION_ID=1 -o apps2.json > log2.txt 2>&1 
