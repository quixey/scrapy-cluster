#!/bin/sh

. ../venv/bin/activate
exec scrapy crawl appannie -L INFO -s FRONTERA_SETTINGS=appannie.spider_settings -s SEEDS_SOURCE=appannie/appannie.txt -s FEED_URI=file:///tmp/appannie.jsons -s FEED_FORMAT=jsonlines -s USER_AGENT="Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36" -s COOKIES_ENABLED=1
