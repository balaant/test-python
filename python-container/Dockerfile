FROM python:3

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN mkdir /tests
COPY ./tests/ /tests/
#RUN pip install  install --upgrade pip && \
#    pip install --no-cache-dir -r requirements.txt
USER root
RUN apt-get update && apt-get install -y pycodestyle
