FROM ubuntu:18.04
MAINTAINER Abe Hoffman "abhoffman@paypal.com"

#### Dependencies ####
RUN mkdir -p /x/

## Canonical ##
RUN apt-get -y update
# System Binaries #
RUN apt-get -y install bc curl
# Compilation Binaries #
RUN apt-get -y install build-essential
RUN apt-get -y install ncurses-dev
RUN apt-get -y install bison
RUN apt-get -y install flex
RUN apt-get -y install gcc-aarch64-linux-gnu
RUN apt-get -y install gcc-arm-linux-gnueabi
RUN apt-get -y install device-tree-compiler

## U-Boot ##
RUN curl -o /x/u-boot-2018.09.tar.bz2 \
            ftp://ftp.denx.de/pub/u-boot/u-boot-2018.09.tar.bz2
RUN tar -xjf /x/u-boot-2018.09.tar.bz2 -C /x/
RUN rm /x/u-boot-2018.09.tar.bz2

#### Scripts ####
RUN mkdir -p /x/scripts
COPY scripts/*.sh /x/scripts/
RUN chmod 0775 /x/scripts/*.sh

#### INIT ####
CMD ["/bin/bash", "/x/scripts/run.sh"]