class Solution:
    def merge(self, ints: List[List[int]]) -> List[List[int]]:
        ints.sort(key=lambda x: x[0])
        res = [ints[0]]

        for t in ints:
            last = res[-1][1]
            if t[0] <= last:
                res[-1][1] = max(last, t[1])
            else:
                res.append(t)
        return res