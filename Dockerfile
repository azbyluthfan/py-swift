# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

EXPOSE 8000
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "gunicorn", "--workers=4", "--bind", "0.0.0.0:8000", "app:app"]