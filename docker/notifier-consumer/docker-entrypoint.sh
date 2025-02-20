#!/bin/sh

set -e

# activate our virtual environment here
. /venv/bin/activate

exec uvicorn notifier_consumer.main:app --host 0.0.0.0 \
     --port 8082 --reload \
     --log-config notifier_consumer/config/log.yaml
