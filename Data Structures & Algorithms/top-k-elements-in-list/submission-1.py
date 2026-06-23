class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mmap = {}
        heap = []

        for num in nums:
            if num not in mmap:
                mmap[num] = 0
            mmap[num] += 1
        
        top = []

        for key in mmap:
            heapq.heappush(heap, (-mmap[key], key))
        while k > 0:
            top.append(heapq.heappop(heap))
            k -= 1
        
        return [x[1] for x in top]
      