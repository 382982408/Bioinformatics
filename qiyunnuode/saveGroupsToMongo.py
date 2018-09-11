#! usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zhang xiong
# Time: 2018/9/10

from getGroup import getGroup
from pymongo import MongoClient

if __name__ == '__main__':
    print(type(getGroup()))
    db = MongoClient("localhost", 27017).qiyunnuode
    collection = db.getGroup
    result = collection.insert(getGroup())
    print(result)