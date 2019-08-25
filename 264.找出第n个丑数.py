# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 12:26:49 2019

@author: yifeng
"""

#264. 找出第n个丑数
# 丑数就是只包含因数2,3,5的正整数，并且后面的丑数必然是前面的丑数通过*2,3,5来的，
# 我们需要做的就是将后面的丑数进行排序，我们用三个指针分别代表*2，*3，*5的index
# 例如已有[1],分别乘2,3,5，得到的丑数中最小的是2，则将*2的指针+1
class Solution(object):
    def nthUglyNumber(self,n):
        dp = [1] # 丑数数列的初始化
        i2 = i3 = i5 = 0 # 三个分别乘2,3,5的指针
        while n>1: #在丑数dp数组中加入n-1个丑数后，停止
            tmp = min(dp[i2]*2,dp[i3]*3,dp[i5]*5) #取三个指针对应相乘后的最小值
            if tmp==dp[i2]*2: #若要加入的最小丑数是*2过来的，则*2的指针+1，即指向下一个丑数
                i2 += 1
            if tmp==dp[i3]*3:
                i3 += 1
            if tmp==dp[i5]*5:
                i5 += 1
            dp.append(tmp)
            n -= 1
        return dp[-1]
        

so = Solution()
so.nthUglyNumber(10)