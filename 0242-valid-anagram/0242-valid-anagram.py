class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        diction = {}
        if len(s) != len(t):
            return False
        for i in s:
            if i not in diction:
                diction[i] = 1
            else:
                diction[i] += 1
        
        for i in t:
            if i not in diction:
                return False
            elif diction[i] <= 0:
                return False
            else:
                diction[i] -= 1
        return True
                