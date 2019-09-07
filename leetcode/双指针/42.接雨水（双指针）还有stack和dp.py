# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 12:31:54 2019

@author: yifeng
"""

# 42.接雨水（双指针）
class Solution:
    def trap(self,height):
        size = len(height)
        if size<=2:
            return 0
        left = 0
        right = size-1
        left_max = height[left]
        right_max = height[right]
        volumn = 0
        while left<right:
            if height[left]<height[right]:
                if left_max>height[left]:
                    volumn += left_max-height[left]
                else:
                    left_max = height[left]
                left += 1
            else:
                if right_max>height[right]:
                    volumn += right_max-height[right]
                else:
                    right_max = height[right]
                right -= 1
        return volumn
height = [0,1,0,2,1,0,1,3,2,1,2,1]
so = Solution()
so.trap(height)