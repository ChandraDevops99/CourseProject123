#!/bin/sh
# wait_for_db.sh

set -e

host="$DB_HOST"
port="$DB_PORT"

echo "Waiting for database at $host:$port..."

# Wait until the database port is open
while ! nc -z "$host" "$port"; do
  echo "Waiting for database at $host:$port..."
  sleep 2
done

echo "Database is up!"
exec "$@"