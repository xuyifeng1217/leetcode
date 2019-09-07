# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 14:36:04 2019

@author: yifeng
"""
# 8. 字符串转换整数 (atoi)
import re
class Solution:
    def myAtoi(self,s):
        res = max(min(int(*re.findall('^[\-\+]?\d+',s.lstrip())),2**31),-2**31-1)
        return res

##正则表达式
#    ^:匹配字符串开头
#    [\-\+]： 对单个字符确定范围
#    ？：前一个字符0次或1次扩展 
#    \d:数字
#    \w:单词字符，等价于[A‐Za‐z0‐9_]
#    \D：一个非数字字符
#s = 'whatis your999 problem'
#re.findall('\d+',s)
