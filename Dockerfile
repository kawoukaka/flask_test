From centos:latest
USER root

ENV http_proxy="http://one.proxy.att.com:8080"
ENV https_proxy="http://one.proxy.att.com:8080"
ENV HTTPS_PROXY="http://one.proxy.att.com:8080"
ENV HTTPS_PROXY="http://one.proxy.att.com:8080"
ENV no_proxy="127.0.0.1"

RUN yum update -y
RUN yum install -y httpd net tools
RUN easy_install pip
RUN pip install ansible
RUN yum install -y python-devel

COPY ./requirements.txt .
RUN pip install -r requirements.txt


ENTRYPOINT apachectl "-DFOREGROUND"
