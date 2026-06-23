class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        path = []
        chars = {'2': 'abc', '3': 'def',
             '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs',
             '8': 'tuv', '9': 'wxyz'}
        if digits == '':
            return []
            
        def backtrack(i, path):
            if len(path) == len(digits):
                r = ''.join(path)
                res.append(r)
                return
            
            for j in chars[digits[i]]:
                path.append(j)
                backtrack(i + 1, path)
                path.pop()
        backtrack(0, path)
        return res
                    