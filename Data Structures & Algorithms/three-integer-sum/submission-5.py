class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        
        nums = sorted(nums)

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                pSum = nums[j] + nums[k] + nums[i]
                if pSum > 0:
                    k -= 1
                elif pSum < 0:
                    j += 1
                else:
                    sub = [nums[i], nums[j], nums[k]]
                    out.append(sub)
                    j += 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1

        return out


