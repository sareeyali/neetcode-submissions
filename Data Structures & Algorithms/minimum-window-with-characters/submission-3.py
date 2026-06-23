class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        
        needCount = {}
        for c in t:
            needCount[c] = 1 + needCount.get(c, 0)

        window = {}
        l = 0 # left pointer
        have = 0 # have must = need
        opt = float('inf') # shortest length
        optStr = [-1, -1]
        need = len(needCount)

        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)

            if (s[r] in needCount and 
            window[s[r]] == needCount[s[r]]):
                have += 1

            while have == need:
                if (r - l + 1) < opt:
                    opt = r - l + 1
                    optStr = [l, r]

                window[s[l]] -= 1
                if (s[l] in needCount and 
                window[s[l]] < needCount[s[l]]):
                    have -= 1
                l += 1
        l, r = optStr
        return s[l : r + 1] if opt != float('inf') else ""

                