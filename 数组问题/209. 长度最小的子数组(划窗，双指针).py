# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 21:11:54 2019

@author: yifeng
"""
# 划窗，双指针
class Solution:
    def minSubArrayLen(self, s, nums):
        size = len(nums)
        if size<1 or sum(nums)<s:
            return 0
        l=r=0
        min_len = float('inf')
        window = 0
        while r<size:
            window += nums[r]
            r += 1
            while window>=s:
                if min_len>r-l:
                    min_len = r-l
                window -= nums[l]
                l += 1
        return min_len
            

nums = [2,3,1,2,4,3]
s = 7
so = Solution()
so.minSubArrayLen(s,nums)
