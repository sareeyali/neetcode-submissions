class Solution:
    def eraseOverlapIntervals(self, ints: List[List[int]]) -> int:
        ints.sort(key = lambda x: x[0])
        res = 0
        end = ints[0][1]

        for i in ints[1:]:
            if i[0] >= end:
                end = i[1]
            else:
                res += 1
                end = min(i[1], end)

        return res