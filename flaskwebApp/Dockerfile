FROM ubuntu 

RUN apt-get update && \
    apt-get install -y python3 python3-pip

COPY . /opt/

RUN pip3 install flask

CMD ["python3", "/opt/webapp.py"]

