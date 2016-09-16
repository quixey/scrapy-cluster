#!/bin/sh

. ../venv/bin/activate
exec scrapy crawl yellowpages -o yp_0.json -t json -L INFO -s FRONTERA_SETTINGS=frontier.spider_settings -s SEEDS_SOURCE=seeds_es_smp.txt -s SPIDER_PARTITION_ID=0
