#! usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zhang xiong
# Time: 2018/4/9

import pandas as pd

if __name__ == '__main__':
    fn = open('MT_NEW.txt','w',encoding="utf-8")
    with open("20170911_zxw_3s_GSA_Genergy_FinalReport_standard.txt", encoding="utf-8") as f:
        for eachline in f:
            try:
                if eachline.strip().split('\t')[1] == 'MT':
                    fn.write(eachline)
                else:
                    continue
            except:
                fn.write(eachline)


