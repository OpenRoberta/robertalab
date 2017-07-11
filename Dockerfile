FROM ubuntu

RUN apt update && apt upgrade -y && apt install -y git phantomjs maven default-jdk gcc-arm-none-eabi srecord libssl-dev wget unzip && apt-get clean

RUN wget -q https://github.com/OpenRoberta/robertalab/archive/master.zip && \
	unzip master.zip && \
	rm master.zip


WORKDIR /robertalab-master/OpenRobertaParent
RUN mvn clean install


WORKDIR /robertalab-master
RUN /robertalab-master/ora.sh --createemptydb OpenRobertaServer/db-2.2.0/openroberta-db

EXPOSE 1999
CMD ["/robertalab-master/ora.sh", "--start-from-git"]
