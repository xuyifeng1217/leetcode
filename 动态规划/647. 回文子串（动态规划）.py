# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 11:06:35 2019

@author: yifeng
"""

class Solution:
    def countSubstrings(self, s):
        # 计算这个字符串有多少个回文子串
        size = len(s)
        if size<=1:
            return size
        dp = [[0]*size for _ in range(size)]
        
        #从上往下，从左往右遍历，包含l==r
        for r in range(size):
            for l in range(r+1):
                #若s[l]==s[r]，则看s[l:r+1]的长度是否小于3或s[l+1:r-1]是否为回文
                if s[l]==s[r] and (r-l<=2 or dp[l+1][r-1]==1):
                    dp[l][r] = 1
        return sum([sum(x) for x in dp])
    
s = "aaa"
so = Solution()
so.countSubstrings(s)
