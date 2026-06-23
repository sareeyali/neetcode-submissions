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

            for i in range(first, first + groupSize):
                if i not in cards:
                    return False
                cards[i] -= 1
                if cards[i] == 0:
                    if i != heap[0]:
                        return False
                    heapq.heappop(heap)
        return True
