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
import os

print("#############################################################################")
print("                                Download OFA IPs                             ")
print("                                                                             ")
print("     export api_url=https://app.onefirewall.com/api/v1/ips            ")
print("     export api_jwt_key=xxxxxxxxx                                            ")
print("                                                                             ")
print("#############################################################################")
print("")

list_of_ips = 'list_of_ips.txt'
list_of_ips_file = open(list_of_ips,'w')

config_json = {}

api_url = os.getenv('api_url')
api_jwt_key = os.getenv('api_jwt_key')

print(api_url)

max_ts = int(time.time()) - (3600) # Starting scanning from the last hour
max_loops_of_fail = 3

print(time.time())

while True:
    url = api_url + "?ts=" + str(max_ts)
    try:
        response_json = requests.get(url,  headers={"Authorization":api_jwt_key}).json()

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

        max_loops_of_fail = 3
        break
        if len(response_json['body']) == 0:
            break
    except:
        max_loops_of_fail -= 1
        if (max_loops_of_fail<=0):
            print("OneFirewall API is down")
            break


print("###################################################1")
print("###################################################1")
