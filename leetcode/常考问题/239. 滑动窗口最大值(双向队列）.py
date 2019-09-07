# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 16:05:20 2019

@author: yifeng
"""

class Solution:
    def maxSlidingWindow(self, nums, k):
        queue = [] # 滑动窗口，注意：保存的是索引值
        res = []
        if not nums:
            return
        for i in range(len(nums)):
            if i>k and i==queue[0]+k: #若满足条件式，说明index queue[0]不应该在划窗中
                queue.pop(0)
                
            # 如果划窗非空，且新加hjmk,入的数比队列后排的数要大，则把这些数弹出
            # 因为它们永远不会是最大值
            while queue and nums[i]>nums[queue[-1]]: #
                queue.pop(-1)
                
            queue.append(i) 
            # 队首一定是划窗的最大值的index
            if i>=k-1:
                res.append(nums[queue[0]])
        return res
nums = [1,3,-1,-3,5,3,6,7]
k = 3
so = Solution()
so.maxSlidingWindow(nums,k)