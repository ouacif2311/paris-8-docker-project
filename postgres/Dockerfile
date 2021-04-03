FROM postgres:alpine

COPY *.sql /docker-entrypoint-initdb.d/

ADD setup.sql /docker-entrypoint-initdb.d

RUN mkdir /mnt/data

RUN chmod a+r /docker-entrypoint-initdb.d/*