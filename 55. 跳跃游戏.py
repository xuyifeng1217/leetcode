# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 17:03:51 2019

@author: yifeng
"""

class Solution:
    def canJump(self,nums):
        now = 0
        max_d = 0
        while now<=max_d: #现在的位置小于当前能达到的最大位置
            next_d = now+nums[now]
            max_d = max(next_d,max_d)
            if max_d>=len(nums)-1:
                return True
            now += 1
        return False
nums = [3,2,1,0,4]
so = Solution()
so.canJump(nums)