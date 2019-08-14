# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 22:24:02 2019

@author: yifeng
"""

class Solution:
    def maximalRectangle(self, matrix):
        max_area = 0
        dp = [[0]*len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]=='0': 
                    continue
                width = dp[i][j] = dp[i][j-1] + 1 if j else 1
                
                #计算以i,j为右下角的最大矩形面积
                for k in range(i,-1,-1):#逐渐高度+1
                    width = min(width,dp[k][j])
                    cur_area = width*(i-k+1)
                    max_area = max(max_area,cur_area)
        print(dp)
        return max_area
    
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
so = Solution()
so.maximalRectangle(matrix)