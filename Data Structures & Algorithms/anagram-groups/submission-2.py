class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqMap = {}
        for word in strs:
            freq = [0] * 26
            for c in word:
                freq[ord(c) - ord("a")] += 1
            freq = tuple(freq)
            if freq not in freqMap:
                freqMap[freq] = []
            freqMap[freq].append(word)
        return list(freqMap.values())

                

        