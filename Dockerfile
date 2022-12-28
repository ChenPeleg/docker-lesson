FROM python:3.11.1-slim-buster
ENV PYTHONUNBUFFERED=1
RUN apt-get update \
    && apt-get -y install libpq-dev gcc
WORKDIR /django
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt