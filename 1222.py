#! usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zhang xiong
# Time: 2018/2/27

lis = [1,2,3,4]

with open('test.txt', 'w') as d:
    d.writelines([(str(i) + "\t") for i in lis])