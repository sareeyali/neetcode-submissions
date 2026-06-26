class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count frequencies
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        # make a heap by pushing into a list with
        # heappush() make sure the val is pushed as
        # x[0] since that is what heap looks at
        heap = []
        for key, val in freq.items():
            heapq.heappush(heap, (val, key))

            # keep popping when heap gets > k
            if len(heap) > k:
                heapq.heappop(heap)

        # return the val which is x[1]
        return [x[1] for x in heap]
        