# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 20:32:40 2019

@author: yifeng
"""

#1042. 不邻接植花 (图)
from collections import defaultdict
class Solution(object):
    def gardenNoAdj(self, N, paths):
        garden_flower = {} # 记录已经种过花的花园种的是哪种花
        graph = defaultdict(list) # 记录花园的与哪几个花园相邻
        
        for p in paths:
            graph[p[0]].append(p[1])
            graph[p[1]].append(p[0])
        
        res = []
        flowers = set({1,2,3,4})
        # 从第一个花园开始，依次种花，遍历相连的花园都种了啥，然后看看这个花园可以种啥
        for g in range(1,N+1):
            have_flowers = []
            for neighbor in graph[g]:
                if neighbor in garden_flower:
                    have_flowers.append(garden_flower[neighbor])
            if have_flowers: # 若相邻花园有种过花，则这个花园种其它的
                this_garden_flower = (flowers-set(have_flowers)).pop()
            else: # 否则，种1
                this_garden_flower = 1
            garden_flower[g] = this_garden_flower
            res.append(this_garden_flower)
        return res
                
N = 3
paths = [[1,2],[2,3],[3,1]]
so = Solution()
so.gardenNoAdj(N,paths)
