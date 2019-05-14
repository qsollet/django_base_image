FROM python:3.6-alpine

MAINTAINER quentin@sollet.fr

RUN apk update
RUN apk add postgresql-libs
RUN apk add --virtual .build-deps gcc musl-dev postgresql-dev
RUN pip install --no-cache-dir psycopg2-binary gunicorn
RUN apk --purge del .build-deps

COPY scripts/* /usr/local/bin/

ENV GUNICORN_BIND_IP 0.0.0.0
ENV GUNICORN_BIND_PORT 80
ENV GUNICORN_WORKER 2

ONBUILD WORKDIR /src
ONBUILD COPY . /src
ONBUILD RUN pre-build
ONBUILD RUN import-cron
ONBUILD RUN pip install -r requirements.txt

EXPOSE 80

CMD ["run-django"]
