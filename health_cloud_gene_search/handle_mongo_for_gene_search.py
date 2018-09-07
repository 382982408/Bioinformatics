#! usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zhang xiong
# Time: 2018/9/5

from pymongo import MongoClient
from pprint import pprint
import io
from bson.son import SON

# 从输入的文本文件中读取流，以便后续的切出基因名
def read_txt():
    with io.open("primary_data.txt", "r", encoding="utf-8") as f:
        return f.readlines()

# 连接mongodb，使用聚合查询
def process(genename):
    db = MongoClient("localhost", 27017).genetell
    collection = db.female_data
    pipeline = [
        {"$unwind" : "$toReports"},
        {"$match":{"toReports.geneName" : genename}},
        {"$project" :
            {"toReports.proDescrip" : 1}
        }
    ]
    try:
        # python字典中可以用get方法，可以设置默认值，如果取值不到，可以设置返回默认值
        gene_description = list(collection.aggregate(pipeline))[0].get("toReports", "").get("proDescrip", "")
    except:
        gene_description = ""
    return gene_description

def main():
    f_result = open("result.txt", "a")
    for eachline in read_txt():
        try:
            genename = eachline.split("\t")[2]
            gene_description = process(genename)
            f_result.write(eachline.strip() + "\t" + gene_description.strip() + "\n")
        except:
            f_result.write(eachline)
    f_result.close()



if __name__ == '__main__':
    main()