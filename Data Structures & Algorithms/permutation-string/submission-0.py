from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1) - 1
        freq = Counter(s1)
        curr = Counter()
        count = 0

        for r in range(len(s2)):
            curr[s2[r]] += 1
            if (r - l + 1) > len(s1):
                curr[s2[l]] -= 1
                l += 1
            if freq == curr:
                return True  
        return False