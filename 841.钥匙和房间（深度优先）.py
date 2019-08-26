# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 22:05:14 2019

@author: yifeng
"""

#=================================
from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms):
        visited = set([0])
        queue = deque() # 栈
        queue.append(0)
        while queue:
            room = queue.pop() #弹出
            for key in rooms[room]:
                if key not in visited: #若没访问过，加入栈，和visited
                    visited.add(key)
                    queue.append(key)
        return len(visited)==len(rooms)
rooms = [[1,3],[3,0,1],[2],[0]]
so = Solution()
so.canVisitAllRooms(rooms)