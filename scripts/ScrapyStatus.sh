#!/bin/sh

. venv/bin/activate
cd kafka-monitor
./kafka_monitor.py feed '{"appid":"testapp", "uuid": "junk"}'
