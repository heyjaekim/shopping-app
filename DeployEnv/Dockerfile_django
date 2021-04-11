FROM python:3

MAINTAINER nocope

WORKDIR /home/fc_django
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN rm requirements.txt

EXPOSE 8000