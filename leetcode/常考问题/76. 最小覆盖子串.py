# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 19:58:10 2019

@author: yifeng
"""
from collections import Counter
class Solution:
    def minWindow(self, s, t):
        dict_t = Counter(t)
        window = Counter()
        l = r = 0
        min_len = float('inf')
        res = ''
        while r<len(s):
            window[s[r]] += 1
            r += 1
            while all(map(lambda x:window[x]>=dict_t[x],dict_t.keys())):
                if r-l<min_len:
                    min_len = r-l
                    res = s[l:(r)]
                window[s[l]] -= 1
                l += 1
#            r += 1
        return res
                
        
        
s = 'abc'
t = 'a'
so = Solution()
so.minWindow(s,t)