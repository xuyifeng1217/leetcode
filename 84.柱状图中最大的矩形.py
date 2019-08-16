# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 12:23:53 2019

@author: yifeng
"""
#84.柱状图中最大的矩形
# 栈的方法
class Solution:
    def largestRectangleArea(self, heights):
        stack = [] #栈
        heights = [0]+heights+[0] #首尾加0
        res = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]]>heights[i]:
                tmp = stack.pop()
                res = max(res,heights[tmp]*(i-stack[-1]-1)) # 长*宽
            stack.append(i)
            print(stack)
        return res
heights = [2,4,3,5,3]
so = Solution()
so.largestRectangleArea(heights)




# =====以i为中心的最大面积就是向左向右找到第一个比heights[i]小的index
class Solution:
    def largestRectangleArea(self, heights):
        res = 0
        for i in range(len(heights)):
            left_i = i
            right_i = i
            while left_i>=0 and heights[left_i]>=heights[i]:
                left_i -= 1
            while right_i<len(heights) and heights[right_i]>=heights[i]:
                right_i += 1
            res = max(res,heights[i]*(right_i-left_i-1))
        return res
heights = [2,4,3,5,3]
so = Solution()
so.largestRectangleArea(heights)

# 当我们找i左边第一个小于heights[i]，若heights[i-1]>=heights[i]，那么
# 我们可以直接拿i-1左边第一个小于heights[i-1]与heights[i]去比较

class Solution:
    def largestRectangleArea(self, heights):
        if not heights:
            return 0
        n = len(heights)
        left_i = [0]*n
        right_i = [0]*n
        left_i[0] = 0
        right_i[-1] = n
        res = 0
        for i in range(1,n):
            tmp = i-1
            while tmp>0 and heights[tmp]>=heights[i]:
                tmp = left_i[tmp]
            left_i[i]=tmp
        for i in range(n-2,-1,-1):
            tmp = i+1
            while tmp<n and heights[tmp]>=heights[i]:
                tmp = right_i[tmp]
            right_i[i] = tmp
        print(left_i)
        print(right_i)
        for i in range(n):
            res = max(res,heights[i]*(right_i[i]-left_i[i]-1))
        return res
heights = [2,4,3,5,3]
so = Solution()
so.largestRectangleArea(heights)