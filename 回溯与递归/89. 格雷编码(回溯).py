# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 19:08:18 2019

@author: yifeng
"""
#gray码的集合G(n)，则G(n+1)的集合分为两部分：
# 1.给G(n)的每个格雷的二进制形式前面+0
# 2.把G(n)逆序，在对每个格雷码的二进制前面+1
# <<1表示二进制向左移位1位，空缺补0
class Solution:
    def grayCode(self,n):
        res,head = [0],1
        for i in range(n):
            for j in range(len(res)-1,-1,-1):
                res.append(head+res[j])
            head = head<<1
        return res

so = Solution()
so.grayCode(3)

#class Solution:
#    def __init__(self):
#        self.n = 0
#        self.ans = None
#        self.flag = False
#    def grayCode(self,n):
#        self.n = n
#        self.ans = ['0'*n]
#        self.flag = False
#        self.back(self.ans[0])
#        return self.change(self.ans)
#    def back(self,code):
#        if len(self.ans)==2**self.n:
#            self.flag = True
#            return 
#        for i in range(len(code)):
#            next_code = code[:i]+str((1-int(code[i])))+code[i+1:]
#            if next_code not in self.ans:
#                self.ans.append(next_code)
#                self.back(next_code)
#                if not self.flag:
#                    self.ans.remove(next_code)
#    def change(self,ans):
#        res = []
#        if len(ans)==1:
#            return [0]
#        for i in ans:
#            res.append(int(i,2))
#        return res
        
#===========================
#class Solution:
#    def grayCode(self, n):
#        if n==0:
#            return [0]
#
#        res=[]
#        def back(now,x):
#            if len(now)==n:
#                res.append(int(now,2))
#            elif x==0:
#                back(now+'0',0)
#                back(now+'1',1)
#            else:
#                back(now+'1',0)
#                back(now+'0',1)
#        
#        back('',0)
#        return res

#==========================
#class Solution:
#    def grayCode(self,n):
#        if n==0:
#            return ['0']
#        res = ['0','1']
#        for i in range(n-1):
#            tmp = []
#            for j in res:
#                tmp.append('0'+j)
#            for j in res[::-1]:
#                tmp.append('1'+j)
#            res = tmp
#        for i in range(len(res)):
#            res[i] = int(res[i],2)
#        return res
    
#=======================

