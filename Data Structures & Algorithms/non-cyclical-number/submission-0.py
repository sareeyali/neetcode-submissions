class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            n = self.nextNum(n)
        return n == 1
            
    def nextNum(self, n: int):
        res = 0
        while n:
            d = n % 10
            d = d * d
            res += d
            n = n // 10
        return res