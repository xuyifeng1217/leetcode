# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 15:57:23 2019

@author: yifeng
"""

#class TreeNode(object):
#    def __init__(self,x):
#        self.val = x
#        self.left = None
#        self.right = None

#  深度优先
class Solution(object):
    def  hasPathSum(self,root,sum_):
        if root:
            stack = [(root,root.val)]
            while stack:
                r,v = stack.pop(-1)
                left,right = r.left,r.right
                if left:
                    stack.append((left,v+left.val))
                if right:
                    stack.append((right,v+right.val))
                if not left and not right and (sum_==v):
                    return True
            return False
        return False
   
#====迭代==================
class Solution(object):
    def hasPathSum(self,root, sum_):
        if not root:
            return False
        sum_ -= root.val
        if not root.left and not root.right:
            return sum_==0
        return self.hasPathSum(root.left,sum_) or self.hasPathSum(root.right, sum_)
    
#=====dfs=================
class Solution(object):
    def hasPathSum(self,root,sum_):
        if not root:
            return False
        stack = [(root,sum_-root.val)]
        while stack:
            node,cur_sum = stack.pop()
            if not node.left and not node.right and (cur_sum==0):
                return True
            if node.left:
                stack.append((node.left,cur_sum-node.left.val))
            if node.right:
                stack.append((node.right,cur_sum-node.right.val))
        return False