# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 21:26:11 2019

@author: yifeng
"""
import bisect
def minSubArrayLen(s,nums):
    if not nums: 
        return 0
    for i in range(1,len(nums)):
        nums[i] += nums[i-1]
#    print(nums)
    if nums[-1]<s:
        return 0
    res = float('inf')
    nums = [0]+nums
    for i in range(1,len(nums)):
        if nums[i]>=s:
            #二分查找
            loc = bisect.bisect_left(nums,nums[i]-s)
            if nums[i]-nums[loc]>=s:
                res = min(res,i-loc)
            if loc>0:
                res = min(res,i-loc+1)
    return res
    
nums = [2,3,1,2,4,3]
s = 7
minSubArrayLen(s,nums)