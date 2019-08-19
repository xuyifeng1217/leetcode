#17. 电话号码的字母组合
class Solution(object):
    def letterCombinations(self, digits):
        dict_ = {'2':list('abc'),
                '3':list('def'),
                '4':list('ghi'),
                '5':list('jkl'),
                '6':list('mno'),
                '7':list('pqrs'),
                '8':list('tuv'),
                '9':list('wxyz')}
        res = ['']
        for i in digits:
            res = [x+y for x in res for y in dict_[i]]
        return res
    
s = "23"
so = Solution()
res = so.letterCombinations(s)