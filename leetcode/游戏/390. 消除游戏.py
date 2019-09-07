# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 16:17:48 2019

@author: yifeng
"""
# 若n的输出是f(n)，则f(2n) = 2(n-f(n)+1),
# 并且，若n为奇数时，f(n)==f(n-1)
class Solution:
    def lastRemaining(self, n):
        if n==1:
            return 1
        return 2*(n//2 - self.lastRemaining(n//2) + 1)

    
so = Solution()   
so.lastRemaining(19)    


