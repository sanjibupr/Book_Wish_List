FROM postgres:9.6

RUN apt-get update && apt-get install -y postgresql-9.6-postgis-scripts

COPY ./compose/postgres/init-db.sql /docker-entrypoint-initdb.d/init-db.sql
