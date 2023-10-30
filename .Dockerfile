FROM akraradets/base-python

RUN apt update && apt upgrade -y
RUN apt install -y vim


RUN pip3 install numpy
RUN pip3 install pandas
RUN pip3 install matplotlib
RUN pip3 install scikit-learn
RUN pip3 install BaselineRemoval

WORKDIR /root/projects
CMD tail -f /dev/null