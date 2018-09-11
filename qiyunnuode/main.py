#! usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zhang xiong
# Time: 2018/9/10

'''
根据接口获取每个疾病的详细解读信息
'''
from getDisease import getDisease
import json, requests
from pymongo import MongoClient

def getDiseaseName():
    diseases = []
    for group in getDisease():
        # try:
        if group.get("ItemList", ""):
            for eachdisease in group.get("ItemList", ""):
                diseaseName = eachdisease.get("ItemNameKey", "")
                diseases.append(diseaseName)
        # 疾病风险类等几类的ItemList为空，因为有亚分类
        else:
            if group.get("SecondaryGroupList", ""):
                for i in group.get("SecondaryGroupList", ""):
                    for eachdisease in i.get("Items", ""):
                        diseaseName = eachdisease.get("ItemNameKey", "")
                        diseases.append(diseaseName)
    return diseases

def getDescription():
    # resultList = []
    # 连接mongodb
    db = MongoClient("localhost", 27017).qiyunnuode
    collection = db.getDescription

    for diseaseName in getDiseaseName():
        url = "http://www.qynode.com/ItemGenome/GetItem/?barcode=QYER2017050101_W01&version=&itemNameKey=" + diseaseName
        response = requests.get(url)
        content = response.json()
        # resultList.append(content)
        # 保存到mongodb
        result = collection.insert(content)
        print(result)

if __name__ == '__main__':
    getDescription()