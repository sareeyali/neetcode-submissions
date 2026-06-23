class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        idx = {}

        for i in range(len(s)):
            idx[s[i]] = i

        res = []
        size = 0
        end = 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, idx[c])
            
            if i == end:
                res.append(size)
                size = 0
        return res


