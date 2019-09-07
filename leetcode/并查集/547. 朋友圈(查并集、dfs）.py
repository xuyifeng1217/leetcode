# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 20:53:39 2019

@author: yifeng
"""
# 547. 朋友圈
# dfs
class Solution:
    def findCircleNum(self,M):
        n = len(M)
        visited = set() # 访问过的集合
        res = 0
        def dfs(i):
            #基于dfs，将与i连通的节点都放入visited集合
            for j in range(n):
                if M[i][j]==1 and j not in visited:
                    visited.add(j)
                    dfs(j)
                    
        for i in range(n):
            if i not in visited:# 若i没访问过，朋友圈+1
                dfs(i)
                res += 1
        return res
m = [[1,1,0],
 [1,1,1],
 [0,1,1]]
so = Solution()
so.findCircleNum(m)

#====查并集==========================

def findCircleNum(M):
    n = len(M)
    circle = {i:i for i in range(n)} # 初始化，keys:自己，values:自己的爸爸
    def find(i):
        # 找到节点i 的父节点
        if i==circle[i]:
            return i
        circle[i] = find(circle[i])
        return circle[i]
    
    for i in range(n):
        for j in range(i+1,n):
            if M[i][j]==1:
                circle[find(i)] = find(j)
    return sum([1 for k,v in circle.items() if k==v])
m = [[1,1,0],
 [1,1,1],
 [0,1,1]]
findCircleNum(m)

