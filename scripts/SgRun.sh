#!/bin/sh

. venv/bin/activate
cd kafka-monitor
./kafka_monitor.py feed '{"url": "https://seatgeek.com/concert-tickets/alternative", "appid":"sg", "crawlid":"sg1234", "maxdepth":3, "spiderid":"sg" }'
