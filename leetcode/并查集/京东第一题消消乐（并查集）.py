# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 21:43:08 2019

@author: yifeng
"""
class UnionFind:
    def __init__(self,n):
        self.count = n
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
    def find(self,p):
        while p != self.parent[p]:
            p = self.parent[p]
            self.parent[p] = self.parent[self.parent[p]]
        return p
    def is_connected(self,p,q):
        return self.find(p)==self.find(q)
    
    def union(self,p,q):
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p==root_q:
            return
        if self.size[root_p]>self.size[root_q]:
            self.parent[root_q] = root_p
            self.size[root_p] += self.size[root_q]
            
        else:
            self.parent[root_p] = root_q
            self.size[root_q] += self.size[root_p]
        self.count -= 1

arr = [[3,1,2,1,1],
       [1,1,1,1,3],
       [1,1,1,1,1],
       [1,1,1,1,1],
       [3,1,2,2,2]]
m = len(arr)
walk = [[-1,0],[0,1],[1,0],[0,-1]]
def get_index(x,y):
    return x*m+y
max_size = float('inf')
uf = UnionFind(m*m)
for i in range(m):
    for j in range(m):
        if arr[i][j] != 'X':
            for direction in walk:
                next_i,next_j = i+direction[0],j+direction[1]
                if 0<=next_i<m and 0<=next_j<m and arr[i][j]==arr[next_i][next_j]:
                    uf.union(get_index(i,j), get_index(next_i,next_j))
def change():             
        def disappear_id(size):
            max_ = max(size)
            for i,k in enumerate(size):
                if k==max_:
                    return i
        dis_id = disappear_id(uf.size)
        for i in range(m):
            for j in range(m):
                if uf.is_connected(get_index(i,j),dis_id):
                    arr[i][j] = 'X'
max_size = max(uf.size)
while max_size>=3:            
    change()
    # remove 
    for c in range(m): #第c列
        col = [i[c] for i in arr][::-1]
        for i in range(len(col)):
            if col[i]=='X':
                inverse = col[i:]
                break
        count = 0
        while inverse[0]=='X' and count<m:
            inverse = inverse[1:]+[inverse[0]]
            count += 1
        col[i:] = inverse
        col = col[::-1]
        for i in range(m): #第i行
            arr[i][c] = col[i]
    uf = UnionFind(m*m)
    for i in range(m):
        for j in range(m):
            if arr[i][j] != 'X':
                for direction in walk:
                    next_i,next_j = i+direction[0],j+direction[1]
                    if 0<=next_i<m and 0<=next_j<m and arr[i][j]==arr[next_i][next_j]:
                        uf.union(get_index(i,j), get_index(next_i,next_j))
    max_size = max(uf.size)
    print(arr)