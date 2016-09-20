#!/bin/sh

. ../venv/bin/activate
exec scrapy crawl apple -L INFO -s FRONTERA_SETTINGS=frontier.spider_settings -s SPIDER_PARTITION_ID=0 -o apps1.json > log1.txt 2>&1 
