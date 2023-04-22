FROM dokken/ubuntu-20.04:latest

WORKDIR /worker/
RUN  sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list && \
     apt-get clean && \
     apt-get update
RUN apt-get install python3.8 python3.8-dev python3-pip -y
ADD ./run.tar.gz /worker
RUN pip install --upgrade pip -i https://pypi.douban.com/simple \
    && pip install -r ./requirements.txt -i https://pypi.douban.com/simple
RUN apt-get install -y python3-tk
ADD ./run.sh /worker
ADD ./test.py /worker
