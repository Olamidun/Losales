FROM python:3.7-slim-buster
ENV PYTHONUNBUFFERED=1

WORKDIR /losales

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
