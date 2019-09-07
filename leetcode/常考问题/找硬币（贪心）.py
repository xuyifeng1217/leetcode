# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 12:15:34 2019

@author: yifeng
"""

def minCoins(coins,amount):
    m = len(coins)
#    coins.sort()
    dp = [[float('inf')]*(amount+1) for _ in range(m)]
    for i in range(0,amount+1):
        if i%coins[0]==0:
            dp[0][i] = i//coins[0]
    for i in range(1,m):
        for j in range(amount+1):

            for k in range(0,j//coins[i]+1):
                dp[i][j] = min(dp[i][j],dp[i-1][j-coins[i]*k]+k)
    
    return dp[-1][-1]
            
            

coins = [1,3,2]
amount = 11
minCoins(coins,amount)

