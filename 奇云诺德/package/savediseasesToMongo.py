#! usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zhang xiong
# Time: 2018/9/10

from getDisease import getDisease
from pymongo import MongoClient

if __name__ == '__main__':
    print(type(getDisease()))
    db = MongoClient("localhost", 27017).qiyunnuode
    collection = db.getDisease
    result = collection.insert(getDisease())
    print(result)