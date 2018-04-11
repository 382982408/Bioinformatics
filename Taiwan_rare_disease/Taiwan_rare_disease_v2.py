# -*-encoding:utf-8-*-

import json
# import pandas
# # import pickle
import pymongo
import requests
from pprint import pprint

def get_disease_name():          #遍历A-Z和CD
    page_list = []
    for i in range(97,123):
        page_A_Z = chr(i).capitalize()              #或者直接用大写的ASCII，即range(65,91)
        page_list.append(page_A_Z)
    page_list.append("CD")      #增加CD页面
    disease_list_all = []
    for page in page_list:
        response = requests.get(r"http://web.tfrd.org.tw/genehelpDB/GeneHelp/DiseaseDBIndex/%s" % page)
        text = response.text
        disease_list = json.loads(text)['resultString']
        disease_list_all = disease_list_all + disease_list
    for i in disease_list_all:      #去重
        while disease_list_all.count(i) > 1:
            del disease_list_all[disease_list_all.index(i)]
    return disease_list_all

def get_content(disease_name):      #获取疾病详情
    pre_url = r"http://web.tfrd.org.tw/genehelpDB/GeneHelp/DiseaseDBContent/"
    response = requests.post(pre_url + disease_name)
    response.encoding = "utf-8"
    text = response.text
    try:
        text_all = json.loads(text)
        hyperLink = json.loads(text_all["result"])['hyperLink']     #设计的链接
        dis_content = json.loads(text_all["result"])['content']     #所有的内容
    except:
        pass

    disease_new_content = {}
    for each_content in dis_content:
        try:
            disease_new_content[each_content['title']] = each_content['content']
        except:
            continue

    return disease_new_content

if __name__ == '__main__':

    client = pymongo.MongoClient("192.168.233.141",27017)
    db = client.taiwan
    collection = db.hanjianbing

    disease_list_final = get_disease_name()
    num = 1
    for disease_name in disease_list_final:
        try:
            disease_content = get_content(disease_name['nameEN'])
            for key,value in disease_content.items():
                disease_list_final[disease_list_final.index(disease_name)][key.replace(".","_")] = value
            print("已经下载第%s个疾病，疾病名：%s" % (num,disease_name['nameEN']))
        except:
            continue

        pprint(disease_list_final[num - 1])
        num += 1

        collection.insert(disease_list_final[disease_list_final.index(disease_name)])