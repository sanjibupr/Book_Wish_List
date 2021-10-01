#!/bin/bash
# Wait for PostgreSQL to be fully up before continuting.
set -e
cmd="$@"

function postgres_ready(){
python << END
import sys
import psycopg2
try:
    conn = psycopg2.connect(dbname="postgres", user="postgres", host="postgres")
except psycopg2.OperationalError as e:
    print(e)
    sys.exit(-1)
sys.exit(0)
END
}
echo postgres_ready;

until postgres_ready; do
  >&2 echo "Postgres is unavailable - sleeping...."
  sleep 1
done

>&2 echo "Postgres is up - continuing..."

exec $cmd
