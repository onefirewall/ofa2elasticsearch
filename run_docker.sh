#!/bin/bash

#docker images
#docker ps
export api_url=https://app.onefirewall.com/api/v1/ips
export api_jwt_key=

PULL_COMMAND=`docker pull onefirewall/ofa2elasticsearch:latest | grep "Status: Image is up to date for onefirewall/ofa2elasticsearch:latest"`
if [ "$PULL_COMMAND" != "Status: Image is up to date for onefirewall/ofa2elasticsearch:latest" ];then
        echo "Upgrading"
        docker rm -f ofa2elasticsearch
        docker images -a | grep "ofa2elasticsearch" | awk '{print $3}' | xargs docker rmi -f
        docker pull onefirewall/ofa2elasticsearch:latest
        docker run -dit --name ofa2elasticsearch --restart=always -e api_url -e api_jwt_key onefirewall/ofa2elasticsearch:latest
else
        echo "No updated"
fi

