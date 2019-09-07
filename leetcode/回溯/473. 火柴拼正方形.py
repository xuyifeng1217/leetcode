# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 15:43:07 2019

@author: yifeng
"""

class Solution(object):
    def __init__(self):
        self.flag = False
    def makesquare(self,nums):
        sum_ = sum(nums)
        if sum_%4 != 0: # 若总和不能被4整除，就不行
            return False
        target = sum_ / 4
        if max(nums)>target or not nums: #若其中一边大于taget or nums为空，return false
            return False
        n = len(nums)
        nums.sort(reverse=True) #将nums降序，提高效率
        self.back(0,n,nums,[0,0,0,0],target)
        return self.flag
    
    def back(self,i,n,nums,res,target):
            if i==n and res==[target]*4: #出口条件
                self.flag = 1
                return 
            for j in range(4):
                if res[j]+nums[i]<=target:# 第一条边没超target就加上nums[i]
                    if j==0 or res[j] != res[j-1]: #若后面一条边不等于前面一条边
                        res[j] += nums[i]
                        if not self.flag:
                            self.back(i+1,n,nums,res,target)
                        res[j] -= nums[i]
        
arr = [1,1,2,2,2]
so = Solution()
so.makesquare(arr)
