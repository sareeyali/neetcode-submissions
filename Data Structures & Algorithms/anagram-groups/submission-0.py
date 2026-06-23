class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        charMap = {}

        for i in range(len(strs)):
            word = tuple(sorted(strs[i]))
            if word not in charMap:
                charMap[word] = []
            charMap[word].append(strs[i])

        out = []
        for val in charMap.values():
            out.append(val)
        return out