FROM python:3.6-slim

LABEL maintainer=quentin@sollet.fr

COPY scripts/* /usr/local/bin/

RUN useradd --create-home --shell /bin/bash appuser
USER appuser
ENV PATH="/home/appuser/.local/bin:${PATH}"
RUN mkdir /home/appuser/src && mkdir /home/appuser/static && mkdir /home/appuser/media && mkdir ~/data

ENV GUNICORN_BIND_IP 0.0.0.0
ENV GUNICORN_BIND_PORT 8080
ENV GUNICORN_WORKER 2

ENV STATIC_ROOT /home/appuser/static
ENV MEDIA_ROOT /home/appuser/media
ENV DATA_ROOT /home/appuser/data

ONBUILD USER appuser
ONBUILD COPY . /home/appuser/src
ONBUILD WORKDIR /home/appuser/src
ONBUILD RUN pre-build
ONBUILD RUN import-cron
ONBUILD RUN pip install --user gunicorn && pip install --user -r requirements.txt

EXPOSE 8080

CMD ["run-django"]
