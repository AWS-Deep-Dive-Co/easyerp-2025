# pull official base image
FROM ubuntu:20.04

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV SSL_CERT_DIR=/etc/ssl/certs

# install dependencies
RUN apt-get -y update  \
&& apt-get install -y apt-transport-https \
&& apt-get -y install python3 \
&& apt-get -y install python3-pip \
&& apt-get -y install nano \
&& apt-get install -y ca-certificates && update-ca-certificates
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt
RUN apt-get -y install gunicorn
RUN pip3 install celery
#RUN apt install python3.10-gdbm

# copy project
ADD . /app
WORKDIR /app
RUN chmod +x django_start
RUN chmod +x celery_start

EXPOSE 80

ENTRYPOINT [ "./django_start" ]
