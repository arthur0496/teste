FROM python:3.5-stretch

RUN pip install opencv-python psutil matplotlib

WORKDIR /test

ADD . /test