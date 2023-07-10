class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        word = s + s
        if s in word[1 : -1]:
            return True
        return False
        