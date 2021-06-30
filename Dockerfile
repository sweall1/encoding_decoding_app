FROM python:3.7-alpine
MAINTAINER Daniel app

ENV PYTHONUNBUFFED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /encoder_decoder
WORKDIR /encoder_decoder
COPY ./encoder_decoder/ /encoder_decoder

RUN adduser -D user
USER user

