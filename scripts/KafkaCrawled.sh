#!/bin/sh

. venv/bin/activate
cd kafka-monitor
exec ./kafkadump.py dump -t demo.crawled_firehose
