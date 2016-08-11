#!/bin/sh

. venv/bin/activate
cd kafka-monitor
./kafka_monitor.py feed '{"action": "info", "appid":"testapp", "crawlid":"abc1234", "uuid": "junk", "spiderid": "link"}'

