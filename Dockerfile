FROM python:3.9

MAINTAINER Oleksandr Korovii

WORKDIR /api

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /api