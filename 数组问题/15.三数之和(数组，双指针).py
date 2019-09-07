# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 10:53:48 2019

@author: yifeng
"""

# 15。三数之和:数组，双指针
class Solution:
    def threeSum(self, nums):
        res = []
        n = len(nums)
        nums.sort()
        for i in range(n-2):
            if nums[i]>0: break
            if i>0 and nums[i]==nums[i-1]: continue
            j = i+1
            k = n-1
            while j<k:
                sum_ = nums[i]+nums[j]+nums[k]
                if sum_==0:
                    res.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while j<k and nums[j]==nums[j-1]:
                        j += 1
                    while j<k and nums[k]==nums[k+1]:
                        k -= 1
                elif sum_>0:
                    k -= 1
                    while j<k and nums[k]==nums[k+1]:
                        k -= 1
                else:
                    j += 1
                    while j<k and nums[j]==nums[j-1]:
                        j += 1
        return res       
nums = [-1,0,1,2,-1,-4]
so = Solution()
so.threeSum(nums)