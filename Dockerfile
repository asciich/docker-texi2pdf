FROM ubuntu:18.04

MAINTAINER Reto Hasler <reto.hasler@asciich.ch>

ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true

RUN echo "Europe/Zurich" > /etc/timezone && \
    apt-get update && \
    apt-get install -y\
        findutils \
        texinfo \
        texlive \
        texlive-lang-european \
        texlive-lang-german \
        texlive-latex-extra \
        vim \
    &&\
    apt-get clean