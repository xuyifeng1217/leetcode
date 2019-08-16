# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 19:17:25 2019

@author: yifeng
"""
#221. 最大正方形
# 动态规划
#======================================    
class Solution:
    def maximalSquare(self,matrix):
        if not matrix: return 0
        dp = [[0]*len(matrix[0]) for _ in range(len(matrix))]
        maxlen = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]=='0':
                    continue
                if i==0 or j==0:
                    dp[i][j] = int(matrix[i][j])
                else:
                    dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
                maxlen = max(maxlen,dp[i][j])
        print(dp)
        return maxlen**2
    
matrix = [["0","0","1","0"],["1","1","1","1"],["1","1","1","1"],["1","1","1","0"],["1","1","0","0"],["1","1","1","1"],["1","1","1","0"]]
so = Solution()
so.maximalSquare(matrix)    
        
#====================================================================
#遍历(i,j)，得到以(i,j)为右下角的最大正方形面积 
class Solution:
    def maximalSquare(self, matrix):
        wm = [[0]*len(matrix[0]) for _ in range(len(matrix))]
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]=='0':
                    continue
                width = wm[i][j] = wm[i][j-1]+1 if j else 1
                print(wm)
                l = 0
                for k in range(i,-1,-1):
                    l += 1
                    width = min(width,wm[k][j])
                    
                    if l <= width:
                        res = max(res,l**2)
        return res
matrix = [["0","0","1","0"],["1","1","1","1"],["1","1","1","1"],["1","1","1","0"],["1","1","0","0"],["1","1","1","1"],["1","1","1","0"]]
so = Solution()
so.maximalSquare(matrix)