class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
       
        r = max(piles)
        l = 1
        k = r

        while l <= r:
            mid = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p/mid)
            
            if hours <= h:
                k = min(k, mid)
                r = mid - 1
            else:
                l = mid + 1
        return k
            
