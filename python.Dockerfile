FROM python:3.10.13-bookworm

# https://vsupalov.com/docker-arg-env-variable-guide/
# https://bobcares.com/blog/debian_frontendnoninteractive-docker/
ARG DEBIAN_FRONTEND=noninteractive
# Timezone
ENV TZ="Asia/Bangkok"

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

RUN apt install -y build-essential
RUN apt install -y vim

WORKDIR /root/projects

# pipenv
ENV PIPENV_VENV_IN_PROJECT=1
RUN pip install --upgrade pip
RUN pip install pipenv

# Export PDF
RUN apt install -y texlive-xetex texlive-fonts-recommended texlive-plain-generic
RUN apt install -y pandoc
RUN pipenv install

# X410
ENV DISPLAY host.docker.internal:0


RUN apt-get clean && rm -rf /var/lib/apt/lists/*

CMD tail -f /dev/null
# CMD python -m ipykernel_launcher -f $DOCKERNEL_CONNECTION_FILE