# run via docker compose :)

FROM ubuntu:22.04

RUN apt-get update

RUN apt-get -y install socat 

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd

WORKDIR /home/ctf

COPY rev2 .
COPY flag.txt .

USER ctf
CMD socat -ddd TCP4-LISTEN:1024,fork,reuseaddr exec:./rev2,pty,echo=0,raw,iexten=0
