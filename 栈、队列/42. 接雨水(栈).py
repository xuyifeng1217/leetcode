# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 11:37:09 2019

@author: yifeng
"""
class Solution:
    def trap(self,height):
        #对于i个柱子，找出其左边的最高的柱子,和其右边的最高的柱子index
        size = len(height)
        if size<=2:
            return 0
        left = [0]*size
        stack = []
        right = [0]*size
        for i in range(size):
            while stack and height[i]>height[stack[-1]]:
                stack.pop(-1)
            stack.append(i)
            left[i] = stack[0]
        stack = []
        for i in range(size-1,-1,-1):
            while stack and height[i]>height[stack[-1]]:
                stack.pop(-1)
            stack.append(i)
            right[i] = stack[0]
        #对于柱子i，其积水体积为其左右最高柱子的最小值-柱子i
        volumn = 0
        for i in range(size):
            volumn += min(height[left[i]],height[right[i]])-height[i]
    #    print(right)
        return volumn
height = [0,1,0,2,1,0,1,3,2,1,2,1]
so = Solution()
so.trap(height)