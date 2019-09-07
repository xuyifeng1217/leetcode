# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 11:16:58 2019

@author: yifeng
"""

#516. 最长回文子序列
#给定一个字符串s，找到其中最长的回文子序列的长度
class Solution:
    def longestPalindromeSubseq(self,s):
        size = len(s)
        if size<=1:
            return size
        dp = [[0]*size for _ in range(size)]
#        dp[0][0] = 1
        for r in range(size):
            for l in range(r,-1,-1):
                if l==r:
                    dp[l][r] = 1
                else:
                    if s[l]==s[r]:
                        dp[l][r] = dp[l+1][r-1] + 2
                    else:
                        dp[l][r] = max(dp[l][r-1],dp[l+1][r])
        return dp[0][size-1]
s = 'abbabababababab'
so = Solution()
so.longestPalindromeSubseq(s)
                
                