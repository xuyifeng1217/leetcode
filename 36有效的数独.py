# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 22:15:51 2019

@author: yifeng
"""

# 36 有效的数独
import collections

#####################解法二#################
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

#########解法二########################
        
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # 遍历所有数，利用dict，将各个数分别存储于各row,column and box，values为出现的次数
        # 若次数大于1，return False
        n = len(board)
        row = [{} for _ in range(n)]
        column = [{} for _ in range(n)]
        box = [{} for _ in range(n)]
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                box_index = (i//3)*3+j//3 # box_index:0,1,2,3,4,5,6,7,8s
                if num != '.':
                    num = int(num)
                    row[i][num] = row[i].get(num,0)+1
                    column[j][num] = column[j].get(num,0)+1
                    box[box_index][num] = box[box_index].get(num,0)+1
                    
                    if row[i][num]>1 or column[j][num]>1 or box[box_index][num]>1:
                        return False
        return True