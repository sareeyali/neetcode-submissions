class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []
        def backtrack(i):
            if i == len(s):
                res.append(path[:])
                return
            for j in range(i, len(s)):
                if self.isPal(s[i:j+1]):
                    path.append(s[i:j+1])
                    backtrack(j + 1)
                    path.pop()
        backtrack(0)
        return res

    def isPal(self, s: str):
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            r -= 1
            l += 1
        return True

