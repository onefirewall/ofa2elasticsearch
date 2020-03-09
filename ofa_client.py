###################################################
#                                                 #
#      Copyright OneFirewall Alliance LTD         #
#                                                 #
###################################################
import requests
import json
import time
import numpy
import datetime

print("###################################################")
print("            Download OFA IPs                       ")
print("###################################################")
print("")

list_of_ips = 'list_of_ips.txt'
list_of_ips_file = open(list_of_ips,'w')

config_json = {}

try:
    with open('config.json') as json_file:
        config_json = json.load(json_file)
except:
    print("No config.json file found, download the file from https://app.onefirewall.com")
    exit(1)

max_ts = 0

while True:
    url = config_json['api_url'] + "?ts=" + str(max_ts)
    response_json = requests.get(url,  headers={"Authorization":config_json['api_jwt_key']}).json()

    code = response_json['header']['exec_python']

    for i in response_json['body']:

        scoreTimeZero = i['score']
        current_time = int(time.time()) - int(i['ts'])

        exec(code)
        score=int(score)
        
        event_ts = str(datetime.datetime.fromtimestamp(i['ts']).isoformat()) + ".000Z"
        list_of_ips_file.write(i['ip'] + " " + str(int(i['score'])) + " " + str(event_ts) + " " + str(score) + "\n")

        if( max_ts < i['ts']):
            max_ts = i['ts']
    
    #break
    if len(response_json['body']) == 0:
        break

print("###################################################")
