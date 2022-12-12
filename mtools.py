#!/usr/local/bin/python

"""Module for interacting with DataDog/Wormly/Zabbix."""

import os
import time
import pytz
import colorama
import requests
import json
# from configparser import ConfigParser
from datetime import datetime
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import synthetics_api
from datadog_api_client.v1.models import SyntheticsUpdateTestPauseStatusPayload
from datadog_api_client.v1.models import SyntheticsTestPauseStatus
from datadog_api_client.v1.api import downtimes_api
from datadog_api_client.v1.api.downtimes_api import DowntimesApi
from datadog_api_client.v1.model.downtime import Downtime
import maintenance_utility

myjs_hostids = [
    "36304",  # MYJS Docswap - ds-mfs (SG2)
    "43899",  # MYJS Docswap - ds-mfs (SG2) Load Average
    "36303",  # MYJS Docswap - ds-myjs (SG1)
    "36306",  # MYJS Docswap - ds-myjs-id
    "36307",  # MYJS Docswap - ds-myjs-idck
    "40396",  # MYJS OWA
    "45770",  # MYJS OWA - Preprosessing Schedule
    "52739",  # MYJS Serverchat
    "17943",  # MYJS WebServer
    "18151",  # MYJS WebServer (ID)
    "58102",  # MYJSDB centralmyjs transfer
]

cfs_hostids = [
    "70542",  # Jobsdb TH MSite
    "54589",  # Jobsdb TH DesktopSite
    "70641",  # Jobsdb MobileAppApi
    "54252",  # Jobsdb HK DesktopSite
]

colorama.init(autoreset=True)


# Print iterations progress
def printProgressBar(iteration, total, prefix='', suffix='', decimals=1,
                     length=100, fill='█', printEnd="\r"):
    """Create a Simple progress bar."""
    percent = ("{0:." + str(decimals) + "f}").\
        format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()


def displayProgressBar():
    """Generate the progress bar and display on screen."""
    # A List of Items
    items = list(range(0, 57))
    plength = len(items)

    # Initial call to print 0% progress
    printProgressBar(0, plength, prefix='Connecting:', suffix='Complete',
                     length=50)
    for i, item in enumerate(items):
        # Do stuff...
        time.sleep(0.02)
        # Update Progress Bar
        printProgressBar(i + 1, plength, prefix='Connecting:',
                         suffix='Complete', length=50)


def get_wormly_downtimes(hostids, noprint):
    """Get latest set downtime from Wormly for the HostID(s)."""
    results = []
    downtimes=""
    for host in hostids:
        url = "https://api.wormly.com/?key=" + os.getenv('key') + "&cmd=getScheduledDowntimePeriods&response=json&hostid=" + host
        payload = {}
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }
        if not noprint:
            downtimes+=(f"Lastest Downtime for HostID: {host}")
        response = requests.get(url, headers=headers, data=payload)
        data = json.loads(response.text)['periods'][-1]
        results.append({host: data})
        if not noprint:
            downtimes+=(f"On: {data['on']}"+"\n")
            downtimes+=(f"Start: {data['start']}"+"\n")
            downtimes+=(f"End: {data['end']}"+"\n")
            downtimes+=(f"TimeZone: {data['timezone']}"+"\n")
            downtimes+=("-"*80+"\n")
            time.sleep(0.2)
    if noprint:
        return results
    blocks=maintenance_utility.create_block(downtimes)
    return blocks
    # print(response.text)


def set_wormly_downtimes(hostids, start, end, timezone, recurrence, on):
    """Set downtimes in Wormly for the HostID(s)."""
    for host in hostids:
        url = "https://api.wormly.com/?key=" + os.getenv('key') + "&cmd=setScheduledDowntimePeriod&response=json&hostid=" + host + "&start=" + start + "&end=" + end + "&timezone=" + timezone + "&recurrence=" + recurrence + "&on=" + on

        payload = {}
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }
        # print(url)

        response = requests.get(url, headers=headers, data=payload)
        data = json.loads(response.text)
        # pprint(data)
        if data["errorcode"] == 0:
            print(f"Downtime scheduled successfully for HostID: {host}")


def list_synthetic_tests(config, scope, noprint):
    with ApiClient(config) as api_client:
        api_instance = synthetics_api.SyntheticsApi(api_client)
        testIDs = []
        tests_in_scope = []
        synthetic_tests=""
        # example, this endpoint has no required or optional parameters
        try:
            # Get the list of all tests
            api_response = api_instance.list_tests()
            for i, test in enumerate(api_response['tests']):
                if not noprint:
                    if scope == 'live' and str(test['status']) == 'live':
                        tests_in_scope.append(test)
                    elif scope == 'paused' and str(test['status']) == 'paused':
                        tests_in_scope.append(test)
                    elif scope == 'all':
                        tests_in_scope.append(test)
                else:
                    if i != 2:
                        testIDs.append(test['public_id'])
            if noprint:
                return testIDs
            j=1
            for i, t in enumerate(tests_in_scope):
                synthetic_tests+=(f"Test #{i+1}" + "\n")
                synthetic_tests+=(f"Name: {t['name']}" +"\n")
                synthetic_tests+=(f"ID: {t['public_id']}" +"\n")
                synthetic_tests+=(f"TYPE: {t['type']}" +"\n")
                synthetic_tests+=(f"STATUS: {t['status']}" +"\n")
                synthetic_tests+=(f"MESSAGE TO: {t['message']}" +"\n")
                synthetic_tests+=("\n"+("*"*80)+"\n")
                j += 1
            blocks=maintenance_utility.create_block(synthetic_tests)
            return blocks
        except ApiException as e:
            synthetic_tests+=("Exception when calling SyntheticsApi->list_tests: %s\n" % e)


def pause_unpause_all_synthetic_tests(config, state):
    """Pause/Unpause all Synthetic tests."""
    testIDs = list_synthetic_tests(config, all, True)
    blocks=pause_unpause_synthetic_tests(config, testIDs, state)
    return blocks


def pause_unpause_synthetic_tests(config, testIDs, state):
    """Pause/UnPause a specific Synthetic test."""
    with ApiClient(config) as api_client:
        api_instance = synthetics_api.SyntheticsApi(api_client)
        synthetic_tests_pause_unpause=""
        if testIDs:
            for id in testIDs:
                public_id = id
                synthetic_tests_pause_unpause+=("Test ID is : "+public_id+"\n")
                synthetic_tests_pause_unpause+=("State is set to : "+state+"\n")
                synthetic_tests_pause_unpause+=("\n"+("*"*80)+"\n")
                # body = SyntheticsUpdateTestPauseStatusPayload(
                #     new_status=SyntheticsTestPauseStatus(state),
                # )
                # try:
                #     api_response = api_instance.update_test_pause_status(public_id, body)
                # except ApiException as e:
                #     print("Exception when calling SyntheticsApi->update_test_pause_status: %s\n" % e)

    blocks=maintenance_utility.create_block(synthetic_tests_pause_unpause)
    return blocks 

def list_downtimes(config, scope):
    """List all currently scheduled Downtimes."""
    with ApiClient(config) as api_client:
        api_instance = downtimes_api.DowntimesApi(api_client)
        current_only = False
        downtimes=""
        if scope == 'live':
            current_only = True
        try:
            # Get all downtimes
            api_response = api_instance.list_downtimes(current_only=current_only)
            if not len(api_response):
                downtimes+=("********No Downtimes found********")
                return
            found_scheduled = False
            downtimes+=("-"*50+"\n")
            for i, dt in enumerate(api_response):
                if scope == 'scheduled':
                    if not dt['disabled']:
                        found_scheduled = True
                        downtimes+=(f"Downtime #{i+1} :"+"\n")
                        downtimes+=(f"Disabled: {dt['disabled']}"+"\n")
                        downtimes+=(f"Start (POSIX):  {dt['start']}"+"\n")
                        indatetime1 = datetime.fromtimestamp(int(dt['start']))
                        downtimes+=(f'Start in local time: {indatetime1}'+"\n")
                        local1 = pytz.timezone("Asia/Kolkata")
                        toconvert1 = pytz.timezone("Asia/Kuala_Lumpur")
                        localize1 = local1.localize(indatetime1)
                        converted1 = localize1.astimezone(toconvert1)
                        downtimes+=(f'Start in target timezone: {converted1}'+"\n")
                        downtimes+=(f"End (POSIX): {dt['end']}"+ "\n")
                        if(dt['end'] != None):
                            indatetime = datetime.fromtimestamp(int(dt['end']))
                            downtimes+=(f'End in local timezone: {indatetime}'+"\n")
                            local = pytz.timezone("Asia/Kolkata")
                            toconvert = pytz.timezone("Asia/Kuala_Lumpur")
                            localize = local.localize(indatetime)
                            converted = localize.astimezone(toconvert)
                            downtimes+=(f'End in target timezone: {converted}'+"\n")
                        downtimes+=(f"TimeZone: {dt['timezone']}"+"\n")
                        downtimes+=(f"Scope: {['scope']}"+"\n")
                        downtimes+=(f"Message: {dt['message']}"+"\n")
                        downtimes+=("*"*50+"\n")
                else:
                    downtimes+=(f"Downtime #{i+1} :"+"\n")
                    downtimes+=(f"Disabled: {dt['disabled']}"+"\n")
                    downtimes+=(f"Start (POSIX):{dt['start']}"+"\n")
                    indatetime1 = datetime.fromtimestamp(int(dt['start']))
                    downtimes+=(f'Start in local time: {indatetime1}'+"\n")
                    local1 = pytz.timezone("Asia/Kolkata")
                    toconvert1 = pytz.timezone("Asia/Kuala_Lumpur")
                    localize1 = local1.localize(indatetime1)
                    converted1 = localize1.astimezone(toconvert1)
                    downtimes+=(f'Start in target timezone: {converted1}'+"\n")
                    downtimes+=(f"End (POSIX): {dt['end']}"+"\n")
                    if(dt['end'] != None):
                            indatetime = datetime.fromtimestamp(int(dt['end']))
                            downtimes+=(f'End in local timezone: {indatetime}'+"\n")
                            local = pytz.timezone("Asia/Kolkata")
                            toconvert = pytz.timezone("Asia/Kuala_Lumpur")
                            localize = local.localize(indatetime)
                            converted = localize.astimezone(toconvert)
                            downtimes+=(f'End in target timezone: {converted}'+"\n")
                    downtimes+=(f"TimeZone: {dt['timezone']}"+"\n")
                    downtimes+=(f"Scope: {dt['scope']}"+"\n")
                    downtimes+=(f"Message: {dt['message']}"+"\n")
                    downtimes+=("*"*50+"\n")
            if scope == 'scheduled' and (not found_scheduled):
                downtimes+=("********No SCHEDULED Downtimes found********")
        except ApiException as e:
            downtimes+=("Exception when calling DowntimesApi->list_downtimes: %s\n" % e)
    blocks=maintenance_utility.create_block(downtimes)
    return blocks 

def schedule_downtime(config, start, end):
    """Schedule Downtime."""
    body = Downtime(
        message="Another TEST - Scheduling Downtime from API",
        start=start,
        end=end,
        timezone="Asia/Kuala_Lumpur",
        scope=["*"],
    )
    # with ApiClient(config) as api_client:
    #     api_instance = DowntimesApi(api_client)
    #     response = api_instance.create_downtime(body=body)
    downtimes="Downtime Scheduled"
    blocks=maintenance_utility.create_block(downtimes)
    return blocks

def get_zabbix_url(region):
    if region == "hk":
        return os.getenv('ZABBIX_API_URL_HK')
    elif region == "th":
        return os.getenv('ZABBIX_API_URL_TH')


def get_zabbix_auth_token(region):
    """Get AUTH Token for Zabbix API."""
    global ZABBIX_AUTH_TOKEN
    url = get_zabbix_url(region)
    uname = os.getenv('ZABBIX_ADMIN_USER')
    passwd = os.getenv('ZABBIX_ADMIN_PASSWD')
    r = requests.post(url,
                  json={
                      "jsonrpc": "2.0",
                      "method": "user.login",
                      "params": {
                          "user": uname,
                          "password": passwd},
                      "id": 1
                  })
    ZABBIX_AUTH_TOKEN = json.dumps(r.json()["result"], indent=4, sort_keys=True)

def get_zabbix_hosts(region, selected_server):
    get_zabbix_auth_token(region) 
    url = get_zabbix_url(region)
    hosts_list = []
    if(selected_server == '0'):
        if(url == os.getenv('ZABBIX_API_URL_HK')):
            hosts_list = ["HKWEB1", "HKWEB2", "HKWEB3", "HKWEB4", "HKWEB5", "HKWEB6"]
        else:
            hosts_list = ["THWEB1", "THWEB2", "THWEB3", "THWEB4", "THWEB5", "THWEB6"]
    elif(selected_server == '1'):
        if(url == os.getenv('ZABBIX_API_URL_HK')):
            hosts_list = ["HKAGENT1", "HKAGENT2", "HKALAGENT1"]
        else:
            hosts_list = ["THAGENT1"]
    elif(selected_server == '2'):
        if(url == os.getenv('ZABBIX_API_URL_HK')):
            hosts_list = ["HKRELINQUISH1","HKRELINQUISH2"]
        else:
            hosts_list = ["THRELINQUISH1","THRELINQUISH2"]
    auth = ZABBIX_AUTH_TOKEN.strip('\"')
    hosts_mapping = {}
    r = requests.get(url,
                    json={
                        "jsonrpc": "2.0",
                        "method": "host.get",
                        "params": {
                            "filter": {
                                "host": hosts_list
                            }
                        },
                        "auth": auth,
                        "id": 1
                    })
    hosts = json.loads(json.dumps(r.json()["result"], indent=4, sort_keys=True))
    for index in range(len(hosts)):
        hosts_mapping[(hosts[index]['host'])] = hosts[index]['hostid']
    return hosts_mapping

def get_maintenance_details(payload, display_all, region):

    if(region == 'th'):
        timezone = pytz.timezone('Asia/Bangkok')
    elif( region == 'hk'):
        timezone = pytz.timezone('Asia/Hong_Kong')

    get_zabbix_auth_token(region) 
    url = get_zabbix_url(region)
    auth = ZABBIX_AUTH_TOKEN.strip('\"')
    maintenance_mapping = {}
    r = requests.get(url,
                    json={
                        "jsonrpc": "2.0",
                        "method": "maintenance.get",
                        "params": payload,
                        "auth": auth,
                        "id": 1
                    })
    maintenance_list = json.loads(json.dumps(r.json()["result"], indent=4, sort_keys=True))
    if(display_all):
        timeperiod_dict = {}
        for key,value in maintenance_list[0].items():
            if(key == 'active_since' or key == 'active_till'):
                value =  datetime.fromtimestamp(int(value), timezone)
            if(key == 'timeperiods'):
                for k,v in value[0].items():
                    if(k == 'start_date'):
                        start_date =  str(datetime.fromtimestamp(int(v), timezone))
                        value[0]['start_date'] = start_date
            print(key,':',value,sep='')
            
            
    else:
        for index in range(len(maintenance_list)):
            maintenance_mapping["maintenanceid"] = maintenance_list[index]['maintenanceid']
            maintenance_mapping["name"] = maintenance_list[index]['name']
            print(maintenance_mapping)

def schedule_zabbix_downtime(hostid, name, active_since_posix, active_till_posix, payload, region):
    get_zabbix_auth_token(region) 
    url = get_zabbix_url(region)
    auth = ZABBIX_AUTH_TOKEN.strip('\"')
    r = requests.get(url,
                    json={
                        "jsonrpc": "2.0",
                        "method": "maintenance.create",
                        "params": {
                            "name": name,
                            "maintenance_type": "1",
                            "active_since": active_since_posix,
                            "active_till": active_till_posix,
                            "hostids": hostid,
                            "timeperiods": [
                                payload
                            ]
                        },
                        "auth": auth,
                        "id": 1
                    })
    print(json.loads(json.dumps(r.json()["result"], indent=4, sort_keys=True)))

def delete_zabbix_maintenance(maintenance_id, region):
    get_zabbix_auth_token(region) 
    url = get_zabbix_url(region)
    auth = ZABBIX_AUTH_TOKEN.strip('\"')
    r = requests.delete(url,
                        json={
                        "jsonrpc": "2.0",
                        "method": "maintenance.delete",
                        "params": maintenance_id,
                        "auth": auth,
                        "id": 1
                    })
    print(json.loads(json.dumps(r.json()["result"], indent=4, sort_keys=True)))
    print("This maintenance was deleted")
