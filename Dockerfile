FROM ubuntu:18.04
RUN apt-get update
RUN apt-get -y install curl
RUN apt-get -y install python3-pip python-pip
RUN apt-get -y install build-essential libxml2-dev libxslt1-dev python-dev libffi-dev libssl-dev
RUN apt-get -y install tor polipo
ADD requirements/common.txt /root/requirements.txt
RUN pip3 install -r /root/requirements.txt
RUN pip install SocksiPy-branch==1.1
RUN pip install PySocks==1.6.8
RUN echo "* - nofile 16384" >> /etc/security/limits.conf
RUN ulimit -n 16384
RUN service polipo restart
ADD torfleet /root/torfleet
ADD ahmia /root/ahmia
ADD run.sh init.sh /root/
WORKDIR /root/
ENTRYPOINT bash /root/init.sh && bash