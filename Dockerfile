FROM python:3.5-stretch

RUN pip install opencv-python

WORKDIR /test

ADD . /test
