#!/bin/sh

. ../venv/bin/activate
exec python -m frontera.worker.db --config bikeaholics.workersettings
