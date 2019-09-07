# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 21:45:17 2019

@author: yifeng
"""
from collections import Counter
class Solution:
    def findSubstring(self,s,words):
        if len(s)<1 or len(words)<1:
            return []
        res = []
        dict_s = Counter(words)
        step = len(words[0])
        size = len(words)
        l = 0
        for r in range(size*step,len(s)+1):
            string = [s[i:i+step] for i in range(l,r,step)]
            window = Counter(string)
#            if all(map(lambda x:dict_s[x]==window[x],dict_s.keys())):
            if window==dict_s:
                res.append(l)
            l += 1
        return res

s = "barfoothefoobarman"
words = ["foo","bar"]

so = Solution()
so.findSubstring(s,words)
