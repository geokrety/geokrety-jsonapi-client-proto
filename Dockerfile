FROM python:3-alpine

MAINTAINER Mathieu Alorent <contact@geokretymap.org>

COPY requirements.txt /src/requirements.txt
RUN  pip3 install --upgrade pip && pip3 install -r /src/requirements.txt
COPY geokrety_jsonapi_client_proto /src/geokrety_jsonapi_client_proto

WORKDIR /src
EXPOSE 5000

CMD FLASK_DEBUG=1 FLASK_APP=geokrety_jsonapi_client_proto/main.py python -m flask run --host=0.0.0.0
