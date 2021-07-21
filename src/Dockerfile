FROM python:3.7.10-slim-buster
MAINTAINER "Shashwat Kare <skare@cisco.com>"

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt
EXPOSE 7000
CMD python app.py
