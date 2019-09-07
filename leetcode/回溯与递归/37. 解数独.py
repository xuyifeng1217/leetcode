# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 16:09:51 2019

@author: yifeng
"""
from collections import defaultdict
class Solution:
    def __init__(self):
        self.flag = None
        self.rows = None
        self.cols = None
        self.boxs = None
        
    def box_id(self,x,y):
        return (x//3)*3+(y//3)
    
    def solveSudoku(self,board):
        self.flag = False
        m = len(board)
        n = len(board[0])
        self.rows = defaultdict(list)
        self.cols = defaultdict(list)
        self.boxs = defaultdict(list)
        for i in range(m):
            for j in range(n):
                num = board[i][j]
                if num!='.':
                    self.rows[i].append(num)
                    self.cols[j].append(num)
                    box_i = self.box_id(i,j)
                    self.boxs[box_i].append(num)
        
        self.back(board,0,0)
#        print(self.rows)
        
    def isValid(self,num,x,y):
        box_i = self.box_id(x,y)
        if (num in self.rows[x]) or (num in self.cols[y]) or (num in self.boxs[box_i]):
            return False
        else:
            return True
        
    def back(self,board,x,y):
        if x==9:
            self.flag = True
            return
        num = board[x][y]
        if num=='.':
            for i in range(1,10):
                if self.isValid(str(i),x,y):
                    board[x][y] = str(i)
                    self.rows[x].append(str(i))
                    self.cols[y].append(str(i))
                    box_i = self.box_id(x,y)
                    self.boxs[box_i].append(str(i))
                    if y==8:
                        self.back(board,x+1,0)
                    else:
                        self.back(board,x,y+1)
                    if self.flag:
                        return 
                    board[x][y]='.'
                    self.rows[x].remove(str(i))
                    self.cols[y].remove(str(i))
                    self.boxs[box_i].remove(str(i))
        else:
            if y==8:
                self.back(board,x+1,0)
            else:
                self.back(board,x,y+1)
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
so = Solution()
so.solveSudoku(board)