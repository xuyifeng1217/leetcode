# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 22:15:51 2019

@author: yifeng
"""

# 36 有效的数独
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid(arr):
            dict_ = collections.Counter(arr)
            dict_.pop('.')
            if not dict_: return True
            if max(dict_.values())>1:
                return False
            return True
        n = len(board)
        for i in range(n):
            arr = board[i]
            if not is_valid(arr):
                return False
            
        for i in range(n):
            arr = [x[i] for x in board]
            if not is_valid(arr):
                return False
            
        for i in range(0,n,3):
            for j in range(0,n,3):
                arr = [x[j:j+3] for x in board[i:i+3]]
                tmp = []
                for k in arr:
                    tmp.extend(k)
                if not is_valid(tmp):
                    return False
        return True