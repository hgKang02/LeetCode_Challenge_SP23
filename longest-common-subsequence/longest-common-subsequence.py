class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache(maxsize=None)
        def LCS(right, left):
            if right == len(text1) or left == len(text2):
                return 0
            elif text1[right] == text2[left]:
                return 1 + LCS(right + 1, left + 1)
            else: 
                return max(LCS(right + 1, left), LCS(right, left + 1))
        return LCS(0,0)