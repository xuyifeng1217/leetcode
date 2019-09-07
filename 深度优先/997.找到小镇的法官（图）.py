# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 20:12:38 2019

@author: yifeng
"""

# 997.找到小镇的法官（图）

from collections import defaultdict
class Solution(object):
    def findJudge(self,N,trust)：:
        # 构建图,k为被信任，v为信任k的人
        graph = defaultdict(lambda:[])
        for p in trust:
            #信任p[0]，被信任p[1]
            graph[p[1]].append(p[0])
        
        candidate = []
        for i in graph:
            if len(graph[i])==N-1:
                candidate.append(i)
                
        def isJudge(person):
            for i in graph:
                if person in graph[i]:
                    return False
            return True
        
        for i in candidate:
            if isJudge(i):
                return i
        else:
            return -1
N = 4
trust = [[1,2],[2,3]]
so = Solution()
so.findJudge(N,trust)
            
        