FROM texlive/texlive:latest

# RUN ln -snf /usr/share/zoneinfo/$CONTAINER_TIMEZONE /etc/localtime && echo $CONTAINER_TIMEZONE > /etc/timezone

# X410
# ENV DISPLAY host.docker.internal:0.0

WORKDIR /root/projects
CMD tail -f /dev/null