class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()
        seq = {}
        for num in nums:
            numSet.add(num)

        for num in nums:
            if num - 1 not in numSet:
                seq[num] = [num]
                curr = num
                while curr + 1 in numSet:
                    seq[num].append(curr)
                    curr += 1

        maxSeq = 0
        for key in seq:
            maxSeq = max(maxSeq, len(seq[key]))

        return maxSeq
                    
