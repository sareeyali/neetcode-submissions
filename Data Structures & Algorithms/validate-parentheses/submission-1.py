class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mydict = {"]":"[", "}":"{", ")":"("}

        for c in s:
            if c in mydict:
                if stack and stack[-1] == mydict[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False