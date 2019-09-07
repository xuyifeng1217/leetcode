# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 15:34:05 2019

@author: yifeng
"""

class Solution:
    def maxSlidingWindow(self, nums, k):
        size = len(nums)
        if size<1:
            return 
        max_ = -float('inf')
        res = []
        for r in range(k-1,size):
            if r==k-1:
                window = nums[:k]
                max_ = max(window)
            else:
                if nums[r-k]==max_:
                    window = nums[(r-k+1):(r+1)]
                    max_ = max(window)
                else:
                    max_ = max(max_,nums[r])
            res.append(max_)
        return res
            
nums = [1,3,-1,-3,5,3,6,7]
k = 3
so = Solution()
so.maxSlidingWindow(nums,k)