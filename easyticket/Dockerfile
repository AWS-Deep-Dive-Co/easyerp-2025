# pull official base image
FROM ubuntu:20.04

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV SSL_CERT_DIR=/etc/ssl/certs
ENV TZ=UTC
ENV DEBIAN_FRONTEND=noninteractive

# install dependencies
RUN apt-get -y update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
        apt-transport-https \
        python3 \
        python3-pip \
        nano \
        tzdata \
        ca-certificates && \
    update-ca-certificates && \
    ln -fs /usr/share/zoneinfo/UTC /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata

# copy requirements and install Python dependencies
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt
RUN apt-get -y install gunicorn

# copy project
ADD . /app
WORKDIR /app

# make scripts executable
RUN chmod +x django_start
RUN chmod +x createsuperuser

# create data directory for sqlite database and media files
RUN mkdir -p /app/data /app/static /app/media

EXPOSE 80

ENTRYPOINT [ "./django_start" ]
