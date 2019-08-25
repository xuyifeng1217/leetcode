# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 16:23:39 2019

@author: yifeng
"""

'''
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）
使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
'''
import time
#class Solution(object):
#    def numSquares(self,n):
#        dp = [0]*(n+1)
#        dp[1] = 1
#        for i in range(2,n+1):
#            if i*i<n+1:
#                dp[i*i] = 1
#            if dp[i] == 0:
#                min_ = min(dp[j]+dp[i-j] for j in range(1,i//2+1))
#                dp[i] = min_
#        return dp[n]
#                
class Solution(object):
    def numSquares(self,n):
        dp = [i for i in range(n+1)]
        for i in range(1,n+1):
            if i*i<n+1:
                dp[i*i] = 1
            if dp[i] != 1:
                j = 1
                while j*j<i+1:
                    dp[i] = min(dp[i],dp[i-j*j]+1)
                    j += 1
        return dp[n]
   #7168         
s = time.time()
so = Solution()
print(so.numSquares(12))
e = time.time()
print(e-s)