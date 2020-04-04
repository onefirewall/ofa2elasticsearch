# OFA Data 2 ElasticSearch via LogStash

1. Install brew
2. run bash install_logstash.sh

```
docker build . -t ofa2elasticsearch1
export api_url=https://app.onefirewall.com/api/v1/ips 
export api_jwt_key=xxxxxx
ocker run -a stdout -a stderr -e api_url -e api_jwt_key ofa2elasticsearch2

```
