# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 15:54:37 2019

@author: yifeng
"""

#class Solution:
#    def canWinNim(self, n):
#        if n<4:
#            return True
#        queue = []
#        queue.extend([True,True,True])
#        for i in range(4,n+1):
#            tmp = not(queue[0] and queue[1] and queue[2])
#            queue.append(tmp)
#            queue.pop(0)
#        return queue[-1]
#    
class Solution:
    def canWinNim(self, n):
        ans = [0,1,1,1]
        res = ans[n%4]
        return res
    
so = Solution()
so.canWinNim(4)
                