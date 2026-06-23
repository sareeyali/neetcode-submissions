class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        res = s[0]
        length = 1

        for i in range(len(s)):
            # odd length center at i
            l = r = i
            while (l >= 0 and r < len(s) 
            and s[l] == s[r]):
                if r - l + 1 > length:
                    res = s[l:r + 1]
                    length = r - l + 1
                l -= 1
                r += 1

            # even length center at i
            l = i
            r = i + 1
            while (l >= 0 and r < len(s)
            and s[l] == s[r]):
                if r - l + 1 > length:
                    res = s[l:r + 1]
                    length = r - l + 1
                l -= 1
                r += 1
        return res
            
                
