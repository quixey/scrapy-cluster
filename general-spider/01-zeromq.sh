#!/bin/sh

. ../../venv/bin/activate
exec python -m frontera.contrib.messagebus.zeromq.broker
