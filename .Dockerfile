# FROM nvidia/cuda:11.6.0-devel-ubuntu20.04
# FROM nvidia/cuda:11.7.0-cudnn8-devel-ubuntu22.04
FROM ubuntu:22.04

# https://vsupalov.com/docker-arg-env-variable-guide/
# https://bobcares.com/blog/debian_frontendnoninteractive-docker/
ARG DEBIAN_FRONTEND=noninteractive
# Timezone
ENV TZ="Asia/Bangkok"

# like CD command in terminal. it will create directory if path is not existed
RUN apt update && apt upgrade -y
# Set timezone
RUN apt install -y tzdata
RUN ln -snf /usr/share/zoneinfo/$CONTAINER_TIMEZONE /etc/localtime && echo $CONTAINER_TIMEZONE > /etc/timezone

# Set locales
# https://leimao.github.io/blog/Docker-Locale/
RUN apt-get install -y locales
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen
ENV LC_ALL en_US.UTF-8 
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  

RUN apt install -y git vim

# python and pipenv
RUN apt install -y python3 python3-pip
# RUN pip install pipenv
# ENV PIPENV_VENV_IN_PROJECT 1

# X410
# ENV DISPLAY host.docker.internal:0.0

WORKDIR /root/projects
CMD tail -f /dev/null