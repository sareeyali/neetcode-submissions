class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for n, num in enumerate(nums):
            seen[num] = n
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                j = seen[diff]
                if j != i:
                    s = [i, j]
                    return sorted(s)
