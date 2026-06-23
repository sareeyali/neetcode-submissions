class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        dp1 = 1
        dp2 = 1
        for i in range(1, len(s)):
            temp = 0

            if s[i] != '0':
                temp += dp1
            two = s[i-1:i+1]
            if 9 < int(two) < 27:
                temp += dp2
            if temp == 0:
                return 0
            dp2 = dp1
            dp1 = temp
        return dp1
