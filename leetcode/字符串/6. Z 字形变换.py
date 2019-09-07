# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 16:11:35 2019

@author: yifeng
"""

#6. Z 字形变换
# 遍历字符串的时候发现，字符的行坐标是先递增后递减的规律，然后依次放入各分组中
class Solution:
    def convert(self,s,numRows):
        if numRows<2:
            return s
        res = ['' for _ in range(numRows)]
        i = 0
        flag = -1
        for c in s:
            res[i] += c
            if i==0 or i==numRows-1:
                flag *= -1
            i += flag
        return ''.join(res)
s = 'A'
so = Solution()
so.convert(s,1)
#
#class Solution:
#    def convert(self, s, numRows):
#        if numRows<=1:
#            return s
#        res = ''
#        step = numRows*2-2
#        size = len(s)
#        
#        for i in range(numRows):
#            if i==0 or i==numRows-1:
#                while i<size:
#                    res += s[i]
#                    i += step
#            else:
#                c = 0
#                while c*step+i < size:
#                    res += s[c*step+i]
#                    if c*step+step-i<size:
#                        res += s[c*step+step-i]
#                    c += 1
#        return res

