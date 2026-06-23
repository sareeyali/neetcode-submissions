class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new = []
        for num in nums:
            if num not in new:
                new.append(num)
            else:
                return True
        return False
        # sliding window of increasing size from 1-n
        # keep adding elements to new list as long as 
        # the new element is not already in the new list
        # how do we check?? use if not in
