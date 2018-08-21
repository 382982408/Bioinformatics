#! usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zhang xiong
# Time: 2018/4/25

import requests

class Get_video(object):

    def __init__(self, video_link):
        self.video_link = video_link

    def process(self):
        req = requests.get(self.video_link)
        with open("wegene.mp4", "wb") as f:
            f.write(req.content)

if __name__ == '__main__':
    g = Get_video("https://1251412368.vod2.myqcloud.com/vodtransgzp1251412368/9031868223093142472/v.f30.mp4?dockingId=fc0d5d41-ea17-46ee-b45f-f05a58dbf309&storageSource=1")
    g.process()
