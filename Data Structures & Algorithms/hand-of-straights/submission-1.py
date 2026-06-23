class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        cards = {}
        for i in hand:
            cards[i] = 1 + cards.get(i, 0)
        
        heap = list(cards.keys())
        heapq.heapify(heap)

        while heap:
            first = heap[0]

            # go through all values of group of size k 
            # for the values starting from the min of the heap
            for i in range(first, first + groupSize):
                # auto fail if the value needed for the group is 
                # not in the cards you have
                if i not in cards:
                    return False
                # else, use that card! and decrease the count
                cards[i] -= 1
                # if we just used the last card of i value,
                if cards[i] == 0:
                    # then it MUST be the heaps smallest card 
                    # if not then we skipped a smaller card
         #           if i != heap[0]:
         #               return False
                    # 
                    heapq.heappop(heap)
        return True
