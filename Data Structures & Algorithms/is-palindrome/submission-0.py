class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns = ""

        for c in s:
            if c.isalnum():
                ns += c
        ns = ns.lower()
        left = 0
        right = len(ns) - 1

        while left < right:
            if ns[left] != ns[right]:
                return False
            else:
                left += 1
                right -= 1
        return True