# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 22:24:02 2019

@author: yifeng
"""
# 85.最大矩形

#   解法一：栈
class Solution:
    def leetcode84(self,heights):
        #直方图的高，返回最大可形成的矩形面积
        stack = []
        heights = [0]+heights+[0]
        res = 0 
        for i in range(len(heights)):
            while stack and heights[stack[-1]]>heights[i]:
                tmp = stack.pop()
                res = max(res,heights[tmp]*(i-stack[-1]-1))
            stack.append(i)
        return res
    
    def maximalRectangle(self,matrix):
        # 遍历每一行，值为以该行为底边的高，然后计算每一行的最大矩形面积
        dp = [0]*len(matrix[0])
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
#                print(dp)
                # 以i行元素为底的直方图
                dp[j] = dp[j]+1 if matrix[i][j]=='1' else 0
            res = max(res,self.leetcode84(dp))
            
        # 以列的形式计算，也可以
#        dp = [0]*len(matrix)
#        res = 0
#        for i in range(len(matrix[0])):
#            for j in range(len(matrix)):
#                dp[j] = dp[j]+1 if matrix[j][i] == '1' else 0
#            res = max(res,self.leetcode84(dp))
        return res
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
so = Solution()
so.maximalRectangle(matrix)



#=====解法二，遍历（i,j），得到以(i,j)为右下角的最大矩形面积
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

#