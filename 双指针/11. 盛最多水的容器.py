# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 20:01:46 2019

@author: yifeng
"""

class Solution:
    def maxArea(self, height):
        size = len(height)
        l = 0
        r = size-1
        area = 0
        while l<r:
            if height[l]<height[r]:
                area = max(area,height[l]*(r-l))
                l += 1
            else:
                area = max(area,height[r]*(r-l))
                r -= 1
        return area
                
            
        
height = [1,8,6,2,5,4,8,3,7]
so = Solution()
so.maxArea(height)

        