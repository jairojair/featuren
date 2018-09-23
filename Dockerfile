FROM python:3.6-alpine

RUN apk add --update \
	postgresql-dev \
	gcc \
	musl-dev \
	make

RUN pip install --upgrade pip

COPY requirements.txt /
RUN pip install -r requirements.txt
