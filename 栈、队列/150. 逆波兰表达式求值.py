# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 17:28:02 2019

@author: yifeng
"""
class Solution:
    def evalRPN(self, tokens):
        stack = []
        ops = ['+','-','*','/']
#        stack.extend([tokens[0],tokens[1]])
        for i in tokens:
            if i in ops:
                second = float(stack.pop())
                first = float(stack.pop())
                if i=='+':
                    stack.append(second+first)
                if i=='-':
                    stack.append(second-first)
                if i=='*':
                    stack.append(second*first)
                if i=='/':
                    stack.append(second/first)
            else:
                stack.append(i)
        return stack[-1]
                    
    
tokens =["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]   
so =Solution()
so.evalRPN(tokens) 
