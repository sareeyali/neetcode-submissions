class Solution:
    def jump(self, nums: List[int]) -> int:
        curr = 0 # reps end of curr range of possibilities reachable 
        farthest = 0
        res = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, nums[i] + i)
            
            # end of current jumps range
            if i == curr:
                res += 1
                curr = farthest
        return res