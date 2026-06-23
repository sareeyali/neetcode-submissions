class Solution:
    def insert(self, ints: List[List[int]], new: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(ints)):
            if new[1] < ints[i][0]:
                res.append(new)
                return res + ints[i:]

            elif new[0] > ints[i][1]:
                res.append(ints[i])
            
            else:
                new = [
                    min(new[0], ints[i][0]), 
                    max(new[1], ints[i][1]),
                ]
        res.append(new)
        return res
