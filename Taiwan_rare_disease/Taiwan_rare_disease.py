# -*-encoding:utf-8-*-


import json
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
    text_all = json.loads(text)
    hyperLink = json.loads(text_all["result"])['hyperLink']     #设计的链接
    content = json.loads(text_all["result"])['content']     #所有的内容
    try:
        bingyinxue = content[0]['content']      #病因学
    except:
        bingyinxue = ""
    try:
        fashenglv = content[1]['content']      #发生率
    except:
        fashenglv = ""
    try:
        linchuang = content[2]['content']     # 临床表征
    except:
        linchuang = ""
    try:
        inheritance = content[3]['content']    # 遗传模式
    except:
        inheritance = ""
    try:
        diagnosis = content[4]['content']      # 诊断
    except:
        diagnosis = ""
    try:
        zhiliao = content[5]['content']         # 治疗
    except:
        zhiliao = ""
    disease_dict_info = {
        "病因学" : bingyinxue,
    "发生率" : fashenglv,
    "临床表征" : linchuang,
    "遗传模式" : inheritance,
    "诊断" : diagnosis,
    "治疗" : zhiliao,
    }
    return disease_dict_info


if __name__ == '__main__':
    disease_list_final = get_disease_name()
    num = 1
    for disease_name in disease_list_final:
        # try:
        disease_content = get_content(disease_name['nameEN'])
        # except:
        #     continue
        for key,value in disease_content.items():
            disease_list_final[disease_list_final.index(disease_name)][key] = value
        print("已经下载第%s个疾病" % num)
        num += 1

        pprint(disease_list_final[num-2])