FROM python:3.10-alpine
RUN apk add --no-cache --update socat py3-pip

WORKDIR /chal
COPY ./server.py /chal/
COPY ./libCrypto.so /chal/

ENTRYPOINT ["socat", "TCP4-LISTEN:12001,reuseaddr,fork", "EXEC:env PYTHONUNBUFFERED=1 python3 /chal/server.py"]
