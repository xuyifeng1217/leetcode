# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 10:44:39 2019

@author: yifeng
"""
# 204.计算质数

class Solution(object):
    def countPrimes(self,n):
        # 计算小于n的所有质数的个数
        # input: n:int -->质数
        # return：小于n的所有质数的个数
        if n<=2:
            return 0
        ans = [1]*n # 用于判断0-n-1哪些是质数
        ans[0] = ans[1] = 0 # 0,1不是质数
        i = 2 # 2是第一个质数
        while i*i<n+1: #若不是质数，其因子最大不超过sqrt(n)，不然属于浪费计算
            if ans[i]==1: # 依次判断，若ans[i]是质数，其所有的倍数都不会是质数
                ans[i*i:n:i] = [0]*len(ans[i*i:n:i]) # 将其所有倍数的位置变为0，第一个位置
                                                    # 从i*i开始即可，
            i += 1 
        return sum(ans)