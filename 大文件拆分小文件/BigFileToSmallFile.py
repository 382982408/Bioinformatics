#! usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zhang xiong
# Time: 2018/2/27

'''
这个需求很常见，因为一般生物信息学数据比较大，比如sam，vcf，或者gtf，bed都是把所有染色体综合在一起的文件。
如果想根据染色体把大文件拆分成小的文件呢？
比如：ftp://ftp.ncbi.nlm.nih.gov/pub/C ... an/CCDS.current.txt
这个文件里面的基因就有染色体信息，那根据染色体把这个文件拆分成1~22和其它染色体，这样的23个文件

website: http://www.biotrainee.com/thread-1329-1-1.html
'''
import os

def process():
    with open("example.txt", "r") as file:
        for eachline in file:
            if eachline:
                chrom = eachline.strip("\n").split('\t',1)[0]
                if chrom.startswith("chr"):
                    with open("%s\outfile\%s.txt" % (os.getcwd(), chrom), "a+") as out:
                        out.write(eachline)
                else:
                    continue
            else:
                break

if __name__ == '__main__':
    process()