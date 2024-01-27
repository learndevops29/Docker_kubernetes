FROM python:3.6-alpine

RUN pip install flask

EXPOSE 5000

COPY . /opt/

CMD ["python3", "/opt/webapp.py"]

