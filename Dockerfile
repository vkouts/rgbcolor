FROM python:3
MAINTAINER Kouts Vladimir <kvn@nicecode.biz>

ENV TERM=xterm

RUN apt-get update && \
    apt-get install -y git && \
    pip install Flask Flask-Mail flask-sqlalchemy flask-migrate flask-admin flask-login gunicorn
