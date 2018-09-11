#! usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zhang xiong
# Time: 2018/9/10

import requests, json

def getGroup():
    response = requests.get("http://www.qynode.com/ItemGenome/GetGroupList/?barcode=QYER2017050101_W01&version=")
    print(response.json())

if __name__ == '__main__':
    getGroup()