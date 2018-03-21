#!/usr/bin/env python
'''
author: zhangxiong
'''
# encoding:utf-8

'''
目的：从txt文件中提取70万个位点的坐标
'''
import re
import pandas as pd

def process():
    lis = []
    with open("20180105_cb_2s_GSA_Genergy_V1_FinalReport_3rdparty.txt","r") as file:
        for idx,eachline in enumerate(file):
            reg = ".*?(\d+[:\-_]\d+).*"         #-有特殊意义，例如0-9，要转义
            gene_position = re.findall(reg, eachline)
            if gene_position:
                lis.append([idx + 1, gene_position[0]])
            else:
                lis.append([idx + 1, " "])
    f = pd.DataFrame(lis)
    f.to_csv("ok.csv",index=False)




if __name__ == '__main__':
    process()