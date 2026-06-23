import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        heap = [] 

        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        res = []
        for v, f in freq.items():
            heapq.heappush(heap, (f, v))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [x[1] for x in heap]