class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            count = len(word)
            encoded += str(count)
            encoded += "#"
            encoded += word
        return encoded


    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            j = i
            # reads whole integer ex 42# will 
            # inc j till the 4 and 2 are a #
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            
            start = j + 1
            end = start + length
            word = s[start:end]
            decoded.append(word)
            i = end
        return decoded
