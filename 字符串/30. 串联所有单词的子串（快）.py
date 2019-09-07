# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 23:02:26 2019

@author: yifeng
"""
from collections import Counter
class Solution:
    def findSubstring(self,s,words):
        if not s or not words:
            return []
        one_word = len(words[0])
        word_num = len(words)
        dict_ = Counter(words)
        res = []
        for i in range(one_word):
            l = i
            r = i
            cur_cnt = 0
            cur = Counter()
            while r+one_word<len(s):
                word = s[r:r+one_word]
                r += one_word
                cur[word] += 1
                cur_cnt += 1
                while cur[word]>dict_[word]:
                    l_word = s[l:l+one_word]
                    l = l+one_word
                    cur[l_word] -= 1
                    cur_cnt -= 1
                if cur_cnt == word_num:
                    res.append(l)
        return res
s = "barfoothefoobarman"
words = ["foo","bar"]

so = Solution()
so.findSubstring(s,words)