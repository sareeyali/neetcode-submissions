class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqMap = defaultdict(list)
        for word in strs:
            freq = [0] * 26
            for c in word:
                freq[ord(c) - ord("a")] += 1
            freqMap[tuple(freq)].append(word)
        return list(freqMap.values())

                

        