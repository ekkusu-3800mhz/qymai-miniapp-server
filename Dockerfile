FROM ubuntu:20.04

COPY ./ubuntu20_tencent_cloud_sources.list /etc/apt/sources.list

RUN apt update

RUN apt install gcc ca-certificates build-essential \
python3 python3-dev python3-pip \
python3-cffi default-libmysqlclient-dev -y

COPY ./server /app

WORKDIR /app

ENV PYTHONUNBUFFERED=1

RUN pip3 config set global.index-url http://mirrors.cloud.tencent.com/pypi/simple \
&& pip config set global.trusted-host mirrors.cloud.tencent.com

RUN pip3 install --user -r requirements.txt

RUN python3 manage.py makemigrations \
&& python3 manage.py migrate

EXPOSE 80

CMD ["python3", "manage.py", "runserver", "0.0.0.0:80"]
