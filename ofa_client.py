###################################################
#                                                 #
#      Copyright OneFirewall Alliance LTD         #
#                                                 #
###################################################
import requests
import json

print("###################################################")
print("            Download OFA IPs                       ")
print("###################################################")
print("")

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

    if len(response_json['body']) == 0:
        break

    for i in response_json['body']: 
        #print(i['ip'])
        if( max_ts < i['ts']):
            max_ts = i['ts']

print(response_json['header'])

print("###################################################")
