import requests
import json


BASE_URL = "https://jsonmock.hackerrank.com/api/iot_devices/search"

def avgRotorSpeed(statusQuery, parentId):
    rotor_speed_sum = 0
    no_of_matched_devices = 0
    
    # get the first page data 
    res_data = get_devices_data(statusQuery, 1)
    if not res_data:
        return 0
    
    total_devices = res_data['total']
    no_of_pages = res_data['total_pages']
    
    devices = get_devices_with_parent(res_data['data'], parentId)
    no_of_matched_devices += len(devices)
    rotor_speed_sum += get_rotor_speed_sum(devices)
    
    # get remaining pages
    for i in range(2, no_of_pages + 1):
        res_data = get_devices_data(statusQuery, 2)
        devices = get_devices_with_parent(res_data['data'], parentId)
        no_of_matched_devices += len(devices)
        rotor_speed_sum += get_rotor_speed_sum(devices)
        
    if no_of_matched_devices == 0:
        return 0
    
    return rotor_speed_sum/no_of_matched_devices
        
def get_devices_data(statusQuery, pageNo):
    params = {
        "status": statusQuery,
        "page": pageNo
    }
    res = requests.get(BASE_URL, params=params)
    if res.ok:
        res_data = json.loads(res.text)
        return res_data
        
def get_devices_with_parent(devices, parentId):
    devices_with_matching_parent = []
    for device in devices:
        if "parent" not in device:
            continue
        parent = device['parent']
        if parent is None:
            continue
        if parent["id"] == parentId:
            devices_with_matching_parent.append(device)
    return devices_with_matching_parent

def get_rotor_speed_sum(devices):
    sum_ = 0
    for device in devices:
        sum_ += device["operatingParams"]["rotorSpeed"]
    return sum_