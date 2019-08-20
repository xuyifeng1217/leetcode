# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 11:14:23 2019

@author: yifeng
"""
# 八皇后

def conflict(queen_str, current_queen):
    # queen_length是之前保存到额queen_list集合的长度，也可以理解为当前current_queen
    # 皇后的行下标
    queen_length = len(queen_str)
    # 定义是否有位置冲突的标志
    flag = False
    for index in range(queen_length):
        #queen_length-index 主要是控制相邻两行的皇后不能处于对角线上
        # 当前皇后不能与之前的皇后在对角线上和同一列上
        if abs(current_queen-int(queen_str[index])) in (0,queen_length-index):
            flag = True
            break
    return flag

def queens(nums=8, queen_str=''):
    '''
    nums:int, 整个棋盘想要存放皇后的个数
    queen_str: str->指代当前皇后存放之前的所有皇后的集合
    return: final_queens: list-->指代最后符合要求的皇后的位置
    '''
    final_queens = [] #全局参数用来保存解
    
    # 定义递归函数，获取所有八皇后的值
    def back(queen_str):
        # 出口条件很重要, 一般放在最前面就好了
        if len(queen_str) == nums:
            final_queens.append(queen_str)
            return
        for index in range(nums):
            flag = conflict(queen_str,index)
            # 如果当前位置的皇后与之前所有位置的皇后都没有冲突，
            if flag is False:
                back(queen_str+str(index))  #传值操作很重要，在不破坏当前值的情况，
                                            #将所需值传下去，这样就能回溯了

    back(queen_str)
    return final_queens

final_queens = queens(nums=4)
print(final_queens)
print(len(final_queens))

