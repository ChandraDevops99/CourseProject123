#!/bin/bash
# wait_for_db.sh
# Waits for MySQL to be ready before proceeding

set -e

DB_HOST="${DB_HOST:-127.0.0.1}"
DB_PORT="${DB_PORT:-3306}"
DB_USER="${DB_USER:-root}"
DB_PASSWORD="${DB_PASSWORD:-password}"

echo "Waiting for database at $DB_HOST:$DB_PORT..."

# Loop until MySQL is reachable
while ! mysqladmin ping -h"$DB_HOST" -P"$DB_PORT" -u"$DB_USER" -p"$DB_PASSWORD" --silent; do
  echo "Database is unavailable - sleeping 2 seconds..."
  sleep 2
done

echo "Database is up! Proceeding..."