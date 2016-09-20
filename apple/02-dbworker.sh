#!/bin/sh

. ../venv/bin/activate
exec python -m frontera.worker.db --config frontier.workersettings > dblog.txt 2>&1
