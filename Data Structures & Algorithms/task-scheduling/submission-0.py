class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        chars = {}
        for t in tasks:
            if t not in chars:
                chars[t] = 0
            chars[t] += 1

        freqs = 0
        maxf = max(chars.values())

        for c in chars:
            if chars[c] == maxf:
                freqs += 1
                
        idle = (maxf - 1) * (n + 1) + freqs
        return max(len(tasks), idle)

