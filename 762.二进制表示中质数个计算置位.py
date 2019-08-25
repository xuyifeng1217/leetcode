# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 11:25:22 2019

@author: yifeng
"""
# 762. 二进制表示中质数个计算置位
class Solution(object):
    def countPrimeSetBits(self,L,R):
        count = 0
        primes = [2, 3, 5, 7, 11, 13, 17,19]
        prime_idx = [0]*20
        for i in primes:
            prime_idx[i] = 1
            
        for num in range(L,R+1):
            if prime_idx[self.helper(num)]==1:
                count += 1
        return count
        
    def helper(self,num):
        return bin(num).count('1')


