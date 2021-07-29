FROM alpine 

RUN apk add python3 
RUN apk add py3-pip
RUN pip3 install flask

ENV APP_SERVER default
ENV APP_PORT 5000
COPY ./myapp.py /opt/

#ENTRYPOINT ["python3 /opt/myapp.py"]
CMD ["python3","/opt/myapp.py"]


