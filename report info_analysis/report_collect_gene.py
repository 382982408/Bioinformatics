#!/usr/bin/env python
'''
author: zhangxiong
'''
# encoding:utf-8

'''
目的：将奇云诺德的报告另存为txt，然后从txt中找出基因和基因型
'''

import re
import pandas as pd
def process():
    with open("晶能生物-高端全基因组健康管理报告-陈.txt","r",encoding="utf-8") as f:
        text = f.read()
        reg = "(基因位点.*?)基因型评价"
        lis_result = re.findall(reg, text)
        num = 0
        lis_pd = []   #用于pandas写入文件
        gene_name = []
        for each in lis_result:
            each_reg = "(基因位点 ：.*?)(基因名  ：.*?)(基因型 ：.*)"
            each_lis = re.findall(each_reg, each)
            num += 1
            each_lis = list(each_lis[0])        #正则匹配多个出来是元祖，将元祖转为list
            # each_lis[0][1].replace(" ")
            each_lis[0] = re.sub(" ", "", each_lis[0])      #替换里面的空格
            each_lis[1] = re.sub(" ", "", each_lis[1])

            each_lis[0] = re.findall(r"[0-9a-zA-Z-]+", each_lis[0])[0]  #查找匹配id
            each_lis[1] = re.findall(r"[0-9a-zA-Z-]+", each_lis[1])[0]  #查找基因名
            lis_pd.append(each_lis)

            gene_name.append(each_lis[1])

        #将列表用pandas写入csv
        # print(lis_pd)

        # name_lis = ["id", "gene name", "genetype"]
        # file = pd.DataFrame(columns=name_lis, data=lis_pd)
        # file.to_csv("result.csv")

        #将基因名去重
        gene_name = set(gene_name)
        print(gene_name)
        print(len(gene_name))

        with open("gene.txt","w") as gene_file:
            gene_file.write("\n".join(gene_name))


        print("OK")



if __name__ == '__main__':
    process()

