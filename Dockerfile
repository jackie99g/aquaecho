FROM jackie99/aquadebian:latest

RUN pip3.10 install supervisor

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

COPY . /usr/src/app/

RUN pip3.10 install --upgrade pip setuptools

RUN pip3.10 install -r requirements.txt

WORKDIR /usr/src/app
