FROM python:3.7.4-alpine

ADD httpserver.py /

CMD python3 /httpserver.py
