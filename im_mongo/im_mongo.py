#! usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zhang xiong
# Time: 2018/9/6

import pandas as pd
from pymongo import MongoClient
import json
from pprint import pprint


"""
主要用于将dataframe数据写入mongodb
"""

def process():
    db = MongoClient("localhost", 27017).drug
    collection = db.durg

def pan():
    df = pd.read_csv("sss.csv")
    db = MongoClient("localhost", 27017).drug
    collection = db.durg
    # pprint(json.loads(df.head().T.to_json()).values())
    # pprint(type(json.loads(df.head().T.to_json()).values()))
    # pprint(json.loads(df.head().T.to_json()))
    # print("$$" * 20)
    # pprint(type(json.loads(df.head().T.to_json())))
    # 这里用insert_many 也可以，主要是数据结构要注意，如果后面没有加.values()的话，所有数据都是在一个文档里面，是一个数据，如果加了values()，那么每条数据就是一个对象
    collection.insert(json.loads(df.T.to_json()).values())


if __name__ == '__main__':
    pan()