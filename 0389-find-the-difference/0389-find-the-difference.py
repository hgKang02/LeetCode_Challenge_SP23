class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        set1 = {}
        for i in s:
            if i not in set1:
                set1[i] = 1
            else:
                set1[i] += 1
        for i in t:
            if i not in set1:
                return i
            elif set1[i] <= 0:
                return i
            else:
                set1[i] -= 1
        return t[-1]