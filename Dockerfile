FROM    ubuntu:18.04
RUN     apt-get -y update
RUN     apt-get -y install python3
RUN     apt-get -y install python3-pip
RUN     apt-get -y install wget
RUN     apt-get -y install gnupg2
RUN     apt-get -y install gnupg
RUN     apt-get -y install apt-utils
RUN     apt-get -y install default-jre
RUN     apt-get -y install nmap
RUN     apt-get -y install curl
RUN     apt-get -y install wget
RUN     wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | apt-key add -
RUN     apt-get -y install apt-transport-https
RUN     echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | tee -a /etc/apt/sources.list.d/elastic-7.x.list
RUN     apt-get -y update
RUN     apt-get -y install logstash
RUN     rm -f /usr/share/logstash/pipeline/logstash.conf

RUN     pip3 install requests
RUN     pip3 install numpy

RUN     mkdir -p /opt/work_dir
WORKDIR /opt/work_dir
COPY    . ./
CMD     bash run.sh


