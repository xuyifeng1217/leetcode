# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 12:18:32 2019

@author: yifeng
"""
# 动态规划，计算第i柱子的左边最高，和右边最高
class Solution:
    def trap(self,height):
        size = len(height)
        if size<=2:
            return 0
        left = [0]*size
        left[0] = height[0]
        right = [0]*size
        right[-1] = height[-1]
        for i in range(1,size):
            left[i] = max(left[i-1],height[i])
        for i in range(size-2,-1,-1):
            right[i] = max(right[i+1],height[i])
        volumn = 0
        for i in range(size):
            volumn += min(left[i],right[i])-height[i]
        return volumn
height = [0,1,0,2,1,0,1,3,2,1,2,1]
so = Solution()
so.trap(height)            