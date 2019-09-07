# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 17:28:42 2019

@author: yifeng
"""

class Solution:
    def intToRoman(self, num):
#        arr = [1000,500,100,50,10,5,1]
        dict_ = {1000:'M',
                 900:'CM',
                 500:'D',
                 400:'CD',
                 100:'C',
                 90:'XC',
                 50:'L',
                 40:'XL',
                 10:'X',
                 9:'IX',
                 5:'V',
                 4:'IV',
                 1:'I'}
        res = ''
        arr = sorted(dict_.keys(),reverse=True)
        for i in arr:
            mul = num//i
            if mul==0:
                continue
            num -= mul*i
            res += dict_[i]*mul
            if num==0:
                break
        return res

num = 1994
so =Solution()
so.intToRoman(num)     