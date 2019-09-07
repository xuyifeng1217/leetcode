# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 21:14:25 2019

@author: yifeng
"""

# 207.课程表（图，拓扑排序）
# 第一种方法用拓扑排序的方法，即先把入度为0的节点放入队列中，依次从队列中移除，
# 更新移除后的其后继节点的入度，若有入度为0，继续放入队列，直到队列为空，判断移除的个数
# 与节点个数是否一致
from collections import defaultdict,deque
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        clen = len(prerequisites)
        if clen==0:
            return True
        # 记录所有课程节点的入度
        in_degrees = defaultdict(int)
        # 散列表，记录所有课程节点的后继课程
        adj = defaultdict(set)
        for s in prerequisites:
            after,before = s[0],s[1]
            in_degrees[after] += 1
            adj[before].add(after)
            
        c = 0
        queue = deque()
        # 先把所有入度为0的课程放入队列中
        for i in range(0,numCourses):
            if in_degrees[i]==0:
                queue.append(i)
        while queue:
            schedule = queue.popleft()
            c += 1
            for i in adj[schedule]:
                in_degrees[i] -= 1
                if in_degrees[i]==0:
                    queue.append(i)
        return c==numCourses
    
# 第二种方法
class Solution(object):
    def canFinish(self, numCourses, prerequisites):# 深度优先遍历，看是否存在环
        clen = len(prerequisites)
        if clen==0:
            return True
        # 深度优先遍历，判断节点是否访问过
        # 这里设置3个状态
        # 0 对应False，表示节点没有访问过
        # 1 对应True,表示节点已经访问过，在深度优先遍历结束后才置1
        # 2 表示当前正在遍历的节点，如果在深度优先遍历过程中，又遇到状态为2
        # 的节点，就表示这个图中存在环
        visited = [0 for _ in range(numCourses)]
        
        # 逆邻接表，存的是每个结点的前驱结点的集合
        # 想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]
        # 1 在前，0 在后
        inverse_adj = [set() for _ in range(numCourses)]
        for p in prerequisites:
            after,before = p[0],p[1]
            inverse_adj[after].add(before)
        
        for i in range(numCourses):
            # 在遍历过程中，如果发现有环，就退出
            if self.dfs(i, inverse_adj, visited):
                return False
        return True
    
    def dfs(self, vertex, inverse_adj, visited):
        '''
        返回是否有环
        vertex: 结点的索引
        inverse_adj: 逆邻接表，记录的是当前结点的前驱结点的集合
        visited：记录了结点是否被访问过，2表示当前正在DFS这个结点
        return: 是否有环，True为有环
        '''
        # 2 表示这个结点正在访问
        if visited[vertex]==2:
            return True
        if visited[vertex]==1:
            return False
        visited[vertex] = 2
        for precursor in inverse_adj[vertex]:
            # 对其前驱结点遍历，如果有环，就返回True
            if self.dfs(precursor,vertex,visited):
                return True
            
       # 1 表示访问结束
       # 先把vertex这个结点的所有前驱结点都输出之后，再输出自己
        visited[vertex] = 1
        return False
        
num = 2
prerequisites = [[1,0],[0,1]]
so = Solution()
so.canFinish(num,prerequisites)
