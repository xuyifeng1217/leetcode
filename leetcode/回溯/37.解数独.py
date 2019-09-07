# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 21:40:19 2019

@author: yifeng
"""

# 37.解数独

from collections import defaultdict
class Solution(object):
    def __init__(self):
        self.flag = None
        self.rows = None
        self.cols = None
        self.boxs = None
        
    def back(self,board,x,y):
            if x==8 and y==8:
                self.flag = True
                return 
            if board[x][y] == '.':
                for num in range(1,10):
                    if self.isValid(num,x,y):
                        self.rows[x][num] += 1
                        self.cols[y][num] += 1
                        box_idx = self.box_index(x,y)
                        self.boxs[box_idx][num] += 1
                        board[x][y] = str(num)
                        if y==8:
                            self.back(board, x+1, 0)
                        else:
                            self.back(board, x, y+1)
                        if self.flag:
                            return 
                        board[x][y] = '.'
                        del self.rows[x][num]
                        del self.cols[y][num]
                        del self.boxs[box_idx][num]
            else:
                if y==8:
                    self.back(board, x+1, 0)
                else:
                    self.back(board, x, y+1)   
          
    def isValid(self,num,x,y):
        box_idx = self.box_index(x,y)
        if (num in self.rows[x]) or (num in self.cols[y]) or (num in self.boxs[box_idx]):
                return False
        else:
                return True
            
    def box_index(self,x,y):
            return (x//3)*3+(y//3)     
        
    def solveSudoku(self,board):
       
        self.flag = False
        self.rows = [defaultdict(int) for _ in range(9)]
        self.cols = [defaultdict(int) for _ in range(9)]
        self.boxs = [defaultdict(int) for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    self.rows[i][num] += 1
                    self.cols[j][num] += 1
                    box_idx = self.box_index(i,j)
                    self.boxs[box_idx][num] += 1
        self.back(board,0,0)
        
        
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
so = Solution()
so.solveSudoku(board)
            
            