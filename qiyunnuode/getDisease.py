#! usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zhang xiong
# Time: 2018/9/10

'''
根据接口获取每个分组的疾病信息
'''
from getGroup import getGroup
import requests
from pprint import pprint
import json

def getDisease():
    #获取分组
    groups = []
    for eachgroup in getGroup():
        groups.append(eachgroup["GroupNameKey"])
    #根据接口传入每个分组获取每个分组的疾病
    print(groups)
    diseases = []
    for group in groups:
        url = "http://www.qynode.com/ItemGenome/GetItemList/?barcode=QYER2017050101_W01&version=&groupNameKey=" + str(group)
        response = requests.get(url)
        content = response.json()
        diseases.append(content)
    return diseases


if __name__ == '__main__':
    pprint(getDisease())





