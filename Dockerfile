
FROM python:3.7-alpine3.10

RUN pip install flask-restful

COPY app/rest-api.py /opt/rest-api.py

CMD python /opt/rest-api.py
