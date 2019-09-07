# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 17:01:21 2019

@author: yifeng
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 递归法
#class Solution:
#    def __init__(self):
#        self.res = []
#    def inorderTraversal(self, root):
#        self.helper(root,self.res)
#        return self.res
#    
#    def helper(self,root,res):
#        if not root:
#            if not root.left:
#                self.helper(root.left,res)
#            self.res.append(root.val)
#            if not root.right:
#                self.helper(root.right,res)

# 栈     
#  中序遍历
#使用颜色标记节点的状态，新节点为白色，已访问的为灰色
#如果遇到的节点为白色，则将其标记为灰色，然后将其右、自身、左子节点依次入栈
class Solution:
    def inorderTraversal(self,root):
        white,gray = 0,1
        stack = [(white,root)]
        res = []
        while stack:
            color,node = stack.pop()
            if node is None:
                continue
            if color==white:
                stack.append((white,node.right))
                stack.append((gray,node))
                stack.append((white,node.left))
            else:
                res.append(node.val)
        return res
        