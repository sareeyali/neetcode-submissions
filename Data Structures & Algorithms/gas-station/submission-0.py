class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        need = 0
        idx = 0
        for i in range(len(gas)):
            need += (gas[i] - cost[i])
            if need < 0:
                need = 0
                idx = i + 1
        return idx
