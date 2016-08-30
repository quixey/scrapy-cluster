#!/bin/sh

. ../venv/bin/activate
exec scrapy crawl appannie -L INFO -s FRONTERA_SETTINGS=appannie.spider_settings -s SEEDS_SOURCE=appannie/appannie.txt
