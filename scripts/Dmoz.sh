#!/bin/sh

. venv/bin/activate
cd kafka-monitor
./kafka_monitor.py feed '{"url": "http://dmoz.org", "appid":"testapp", "crawlid":"abc1234", "maxdepth":1}'

