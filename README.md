# OFA Data 2 ElasticSearch via LogStash
check the logstash.conf for harcoded configration

## Build
```
docker build . -t ofa2elasticsearch
```

## Run Once
receive a JWT token from https://app.onefirewall.com
```
docker pull onefirewall/ofa2elasticsearch:latest
export api_url=https://app.onefirewall.com/api/v1/ips 
export api_jwt_key=xxxxxx
docker run -a stdout -a stderr -e api_url -e api_jwt_key docker pull onefirewall/ofa2elasticsearch:latest
```
## Run As a docker service
run the below bash script every 10min to receive a new updated version and run it
```
bash run_docker.sh
```
