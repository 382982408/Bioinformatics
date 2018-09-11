#! usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zhang xiong
# Time: 2018/9/11

#! usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zhang xiong
# Time: 2018/9/5

from pymongo import MongoClient
from pprint import pprint
import io
from bson.son import SON

# 从抓取的奇云诺德报告中获取基因描述信息

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def read_txt():
    with io.open("primary_data.txt", "r", encoding="utf-8") as f:
        return f.readlines()

# 连接mongodb，使用聚合查询
def process(genename):
    db = MongoClient("localhost", 27017).qiyunnuode
    collection = db.getDescription
    pipeline = [
        {"$unwind" : "$Sites"},
        {"$match":{"Sites.GeneName" : genename}},
        {"$project" :
            {"Sites.GeneDesc" : 1}
        }
    ]
    gene_description = list(collection.aggregate(pipeline))[0].get("Sites", "").get("GeneDesc", "")
    return gene_description
    # try:
    #     # python字典中可以用get方法，可以设置默认值，如果取值不到，可以设置返回默认值
    #     gene_description = list(collection.aggregate(pipeline))[0].get("toReports", "").get("proDescrip", "")
    # except:
    #     gene_description = ""
    # return gene_description

def main():
    f_result = open("result.txt", "a")
    for eachline in read_txt():
        try:
            genename = eachline.split("\t")[4]
            # 如果处于基因间区，每个位点对应多个基因，则哪个最先查到，就显示哪个基因的描述
            genename_list = genename.strip().split(";")
            if len(genename_list) == 1:
                gene_description = process(genename)
                print(gene_description)
                f_result.write(eachline.strip() + "\t" + gene_description.strip() + "\n")
            elif len(genename.split(";")) > 1:
                for eachgenename in genename_list:
                    gene_description = process(eachgenename)
                    if gene_description:
                        break
                    else:
                        continue
                # 不论能否查询到，都写入文件
                f_result.write(eachline.strip() + "\t" + gene_description.strip() + "\n")
        except:
            f_result.write(eachline)
    f_result.close()

if __name__ == '__main__':
    main()