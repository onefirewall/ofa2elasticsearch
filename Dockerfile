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
RUN     wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | apt-key add -
RUN     apt-get -y install apt-transport-https
RUN     echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | tee -a /etc/apt/sources.list.d/elastic-7.x.list
RUN     apt-get -y update
RUN     apt-get -y install logstash
RUN     pip3 install requests
RUN     pip3 install numpy
COPY    run.sh .
COPY    ofa_2_txt_env_var.py .
#RUN     chmod +x run.sh
#CMD     echo 4
#CMD     echo 5
#CMD     echo 1234567
CMD     bash run.sh
#CMD     logstash --version
#CMD     echo 123456
#RUN     apt-get update -y

