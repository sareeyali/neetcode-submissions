class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        
        pre = 1
        for i in range(len(nums)):
            output[i] = pre
            pre *= nums[i]
        
        suff = 1
        for i in reversed(range(len(nums))):
            output[i] *= suff
            suff *= nums[i]
            print(output)

        return output

    