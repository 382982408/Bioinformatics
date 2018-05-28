#! usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zhang xiong
# Time: 2018/5/28

'''
genetell 报告页面：http://www.genetell.com/report3/report.html#/aa
男性报告位点接口：http://www.genetell.com/getResultByTel.do?id=2017000067
女性报告位点接口：http://www.genetell.com/getResultByTel.do?id=2017000222
'''
import requests,json
from pprint import pprint


def male_parser():
    url = "http://www.genetell.com/getResultByTel.do?id=2017000067"
    response  = requests.get(url)
    data_json = response.json()
    # for i in data_json:
    #     pprint(i)
    #     break
    with open('male_data.json', 'w', encoding="utf-8") as file:
        json.dump(data_json, file, ensure_ascii=False)



def female_parser():
    url = "http://www.genetell.com/getResultByTel.do?id=2017000222"
    response  = requests.get(url)
    data_json = response.json()
    n = 1
    for i in data_json:
        pprint(i)
        n += 1
        if n == 4:
            break
    with open('female_data.json', 'w', encoding="utf-8") as file:
        json.dump(data_json, file, ensure_ascii=False)

if __name__ == '__main__':
    female_parser()
