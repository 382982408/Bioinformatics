#! usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zhang xiong
# Time: 2018/4/8

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def get_proxy():
    headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'}
    proxies_list = []
    #爬取前10页
    for page in range(2):
        url = 'http://www.xicidaili.com/nn/%s' % page
        s = requests.get(url,headers = headers)
        soup = BeautifulSoup(s.text,'lxml')
        ips = soup.select('#ip_list tr')
        # print(ips)
        fp = open('host.txt','w')
        num = 1
        for i in ips:
            try:
                ipp = i.select('td')
                ip = ipp[1].text
                port = ipp[2].text
                is_http = ipp[5].text

                #调用check_proxy方法验证代理是否有效
                ip_host_dict = {str(is_http):str(ip+ ':' + port)}
                if check_proxy(ip_host_dict):
                    proxies_list.append(ip_host_dict)
                    #将合格ip保存下来
                    fp.write(is_http)
                    fp.write('\t')
                    fp.write(ip+ ':' + port)
                    fp.write('\n')
                    print("%s条有效" % num)
                    num += 1
            except Exception as e :
                print (e)
                continue
        fp.close()
    print("代理爬取完毕……")
    return proxies_list

def check_proxy(ip_host_dict):
    url = 'http://v2ex.com'
    #proxies需要以字典传入，例如{'http':'121.31.176.176:8123'}
    is_sucess = False
    res = requests.get(url = url, proxies = ip_host_dict)
    if res.status_code == 200:
        # print(res.content)
        is_sucess = True
    return is_sucess

if __name__ == '__main__':
    # check_proxy({'http':'223.241.78.10:8010'})
    # get_proxy()
    ua = UserAgent()
    print(ua.random)