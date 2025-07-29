FROM python:3.11-slim

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -yqq socat && apt-get install -y python3-pip
RUN pip install pycryptodome
ADD ./server.py server.py
ADD ./flag.txt flag.txt

CMD ["socat", "TCP-L:5000,fork,reuseaddr", "EXEC:'python3 server.py'"]