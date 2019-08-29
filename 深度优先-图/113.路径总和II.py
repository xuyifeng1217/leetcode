# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 16:14:50 2019

@author: yifeng
"""
# 深度优先+回溯
class Solution(object):
    def pathSum(self,root,sum_):
        
        def back(root,s,path):
            if not root.left and not root.right and s==sum_:
                result.append(path)
                return 
            if root.left:
                path_left_copy = path.copy()
                path_left_copy.append(root.left.val)
                back(root.left, s+root.left.val, path_left_copy)
            if root.right:
                path_right_copy = path.copy()
                path_right_copy.append(root.right.val)
                back(root.right, s+root.right.val, path_right_copy)

        result = []
        if not root:
            return result
        back(root, root.val, [root.val])
        return result