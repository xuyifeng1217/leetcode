# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 21:48:36 2019

@author: yifeng
"""
# 299. 猜数字游戏

import collections

# 解法一，漂亮
class Solution:
    def getHint(self, secret, guess):
        
        a = sum([i==j for i,j in zip(secret,guess)])
        b = sum((collections.Counter(secret) & collections.Counter(guess)).values())-a
        return '{}A{}B'.format(a,b)
        
 
# 解法二，
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        n = len(secret)
        res1 = 0
        res2 = 0
        secret_ = []
        guess_ = []
        for i in range(n):
            if secret[i]==guess[i]:
                res1 += 1
            else:
                secret_.append(secret[i])
                guess_.append(guess[i])
        secret_ = collections.Counter(secret_)
        guess_ = collections.Counter(guess_)
        for i in secret_:
            if i in guess_:
                res2 += min(secret_[i],guess_[i])
        
        return '{}A{}B'.format(res1,res2)
               
        
secret = "1807"
guess = "7810"
so = Solution()
so.getHint(secret,guess)

                
        
