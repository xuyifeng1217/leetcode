# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 11:20:49 2019

@author: yifeng
"""        
class UnionFind:
    def __init__(self,n):
        self.count = n
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
    def find(self,p):
        # 查找元素p根节点的编号,并对路径进行压缩
        root = p
        while root!=self.parent[root]:
            root = self.parent[root]
        #此时root就是p的根节点
        #接下来对路径进行压缩，所有访问到的节点都指向root
        while p!=self.parent[p]:
            temp = self.parent[p]
            self.parent[p] = root
            p = temp
        return root
    def is_connected(self,p,q):
        return self.find(p)==self.find(q)
    def union(self,p,q):
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root==q_root:
            return 
        if self.rank[p_root]<self.rank[q_root]:
            self.parent[p_root] = q_root
        elif self.rank[q_root]<self.rank[p_root]:
            self.parent[q_root] = p_root
        else:
            self.parent[p_root] = q_root
            self.rank[q_root] += 1
        self.count -= 1
class Solution:
    def solve(self,grid):
        m = len(grid)
        if m==0:
            return 0
#        n = len(grid[0])
#        water = m*n
        uf = UnionFind(m)
#        walk = [[0,1],[1,0]]
#        def get_index(x,y):
#            return x*n+y
#        def isValid(x,y):
#            if 0<=x<m and 0<=y<n and grid[x][y]=='1':
#                return True
#            return False
#        for i in range(m):
#            for j in range(n):
#                if grid[i][j]=='0':
#                    uf.union(get_index(i,j),water)
#                else:
#                    for direction in walk:
#                        next_i,next_j=i+direction[0],j+direction[1]
#                        if isValid(next_i,next_j):
#                            uf.union(get_index(i,j),get_index(next_i,next_j))
#        return uf.count - 1
        for i in range(m):
            for j in range(i+1,m):
                if grid[i][j]==1:
                    uf.union(i,j)
        return uf.count
                   
grid = [[1,1,0],[1,1,0],[0,0,1]]
so = Solution()
so.findCircleNum(grid)