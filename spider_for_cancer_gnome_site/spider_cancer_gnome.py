#! usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zhang xiong
# Time: 2018/4/5

'''
爬取地址：https://www.mycancergenome.org/
网站介绍：这是一个肿瘤位点用药网站
'''

import requests,lxml
import json
from bs4 import BeautifulSoup
import time
from getProxy.get_proxy import get_proxy
import random
from fake_useragent import UserAgent

ua = UserAgent()
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie':'__utmc=58548534; __utmz=58548534.1522889054.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); mcg_local_data=MFD1nUZbgcQWfgQd1dDNEKslIXsXxIMZh5XWTfcy3MaJgtESs%2B577LMzeKxUg4TZ%2Bxa6rOKIgu05aPSoMl1C6aKOe6mG%2FCLlFCtlGeijn2uaHbkcf5oTWVxDUb9Cl6MQ1Vb5gkBwB2EOpvSOF2rUkxu1XZJvNFd%2FKYU4p8BbDT%2FCbKL%2FYk1rsgy0UdVyocGPWIfP2D8J8SHchDC63PVu6j%2FVadh5kVlNbFIsaORoqCmlHtzn%2BKDHG2lBt43QAXhx8yEE2ObC7Zjis%2FvxsQSyyZ8nC4QM8jA4DtGGpoGMSQJS%2F9RvPiqhOC3wcnWTOM7wrzq2KnB298AYYRbHDCrFpwQeWCTbX6UR4CCItX9S8aCKP7rH1eIh%2FTRxtFVLS%2BABM%2FGxtxK%2BnC6%2BdGS17sD5zwljGs1%2FSXjHg52AI4rCzDutxeU4fVA7HHR5XAkEgUcEQKp0ITMS3e8yOYRrGhu3HsSQjABr5IbllRcvUErc78bh05sf4ErHVQoHt2gr6UL%2B510bf570bbd565180af908552b197f1df9feb941; __utma=58548534.967724668.1522889054.1522904185.1522907900.5; __utmt=1; __utmb=58548534.1.10.1522907900',
    'Host': 'www.mycancergenome.org',
    'Referer': 'https://www.mycancergenome.org/',
    'User-Agent': ua.random,
    'X-Requested-With': 'XMLHttpRequest',
}

def get_diease():
    try:
        #需要加上‘https://’，不然请求失败，
        # 参考https://stackoverflow.com/questions/30770213/no-schema-supplied-and-other-errors-with-using-requests-get
        req = requests.get(url = 'https://www.mycancergenome.org/', proxies = random.choice(proxies_list))
        #decode之后也可以格式化输出
        html = req.content
        # print(html)

        # lxml需要加""
        soup = BeautifulSoup(html,'lxml')
        #格式化输出
        # print(bs.prettify())
        #所有的疾病选项都在option标签中
        option = soup.find_all('option')
        # print(option)
        disease = []
        for each_option in option:
            #返回依然是BS4对象，所以还可以用BS的方法快速提取
            # print(type(option))
            # print(type(each_option))
            #或者这样写each_option.attrs来获取属性，不过返回是字典
            disease_value = each_option.get('value')
            disease_name = each_option.string

            # time.sleep(2,5)

            if disease_name and disease_value:
                disease.append([disease_value, disease_name])
    except:
        get_diease()

    return disease

def get_gene(disease_value):
    url = "https://www.mycancergenome.org/api/sp-genome/get-genes-for-disease/?disease=%s" % disease_value
    response = requests.get(url=url, headers=headers, proxies = random.choice(proxies_list))
    if str(response.status_code) == '200':
        # 可用eval将str转为dict
        # gene_pre = response.text
        # gene = eval(gene_pre)
        gene = response.json()
        print(gene)
        print(type(gene))
    else:
        print('被反爬了，状态码是：%s' % response.status_code)

    #返回一个字典，包含基因名字和gene的value，例如{geneA：12，geneB：13}
    return gene





if __name__ == '__main__':
    proxies_list = get_proxy()
    for disease_value,disease_name in get_diease():
        try:
            gene = get_gene(disease_value)
            print(type(gene))
            print(gene)

            # time.sleep(2,5)
        except:
            continue