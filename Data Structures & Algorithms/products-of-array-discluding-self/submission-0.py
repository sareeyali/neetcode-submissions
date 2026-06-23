class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        
        for i, num in enumerate(nums):
            left = 0
            right = len(nums) - 1
            prod = 1
            while left < i:
                prod *= nums[left]
                left += 1
            while right > i:
                prod *= nums[right]
                right -= 1
            output.append(prod)
        return output