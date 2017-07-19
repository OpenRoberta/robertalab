FROM ubuntu

RUN apt update && apt install -y avrdude avr-libc binutils-avr default-jdk gcc-arm-none-eabi gcc-avr gdb-avr git libssl-dev libusb-0.1-4 maven nbc phantomjs python-pip srecord unzip wget && apt-get clean
RUN pip install uflash

RUN wget -q https://github.com/OpenRoberta/robertalab/archive/master.zip && \
	unzip master.zip && \
	rm master.zip


WORKDIR /robertalab-master/OpenRobertaParent
RUN mvn clean install


WORKDIR /robertalab-master
RUN /robertalab-master/ora.sh --createemptydb OpenRobertaServer/db-2.2.0/openroberta-db

VOLUME /robertalab-master/OpenRobertaServer/db-2.2.0
EXPOSE 1999
CMD ["/robertalab-master/ora.sh", "--start-from-git"]
