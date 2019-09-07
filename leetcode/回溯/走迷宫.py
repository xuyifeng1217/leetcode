# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 15:22:41 2019

@author: yifeng
"""
def isValid(nums,current_position):
    # nums: 指代所给的迷宫
    # current_position:list[int x,y]-->指代当前坐标点位置
    # return boolean-->当前位置是否有效
    pos_x = current_position[0]
    pos_y = current_position[1]
    if pos_x in range(len(nums)) and pos_y in range(len(nums[0])) and \
        nums[pos_x][pos_y]==1:
        return True
    else: 
        return False
    
def maze(nums, start):
    #nums:list[list[int]]-->所给的迷宫
    #start:list[int x,y]-->起点坐标
    #return:  route: list[]
    route = []
    #定义当前点上下左右移动方向的集合
    walk_route = [[-1,0],[0,-1],[0,1],[1,0]]
    # 迷宫的终点
    final_position = [len(nums)-1,len(nums[0])-1]
    
    def back(position=start,pos_list=[start]):
        # 该递归函数的出口
        if position==final_position:
            route.append(pos_list)
            print('successful')
            return 
        pos_x = position[0]
        pos_y = position[1]
        for direction in walk_route:
            next_position = [pos_x+direction[0], pos_y+direction[1]]
            if isValid(nums,next_position):
                pos_list_copy = []
                pos_list_copy.extend(pos_list)
                pos_list_copy.append(next_position)
                nums[pos_x][pos_y] = 0
                back(next_position, pos_list_copy)
                # 如果没有找到出口，则将当前上一个位置0重置为1，回溯
                nums[pos_x][pos_y] = 1
    back()
    return route


nums = [[1, 0, 0, 1, 0, 1], [1, 1, 1, 0, 1, 0], [0, 0, 1, 0, 1, 0], 
        [0, 1, 1, 1, 0, 0], [0, 0, 0, 1, 1, 1], [1, 0, 0, 0, 1, 1]]
start = [0,0]
route = maze(nums,start)