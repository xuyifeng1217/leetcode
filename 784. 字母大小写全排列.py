# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 21:13:48 2019

@author: yifeng
"""
# 784. 字母大小写全排列
class Solution:
    def letterCasePermutation(self, S):
        res = ['']
        for i in S:
            if i.isalpha():
                I = [i.upper(), i.lower()]
                res = [x+y for x in res for y in I]
            else:
                res = [x+i for x in res]
        return res
    
S = "a1b2"
so = Solution()
so.letterCasePermutation(S)