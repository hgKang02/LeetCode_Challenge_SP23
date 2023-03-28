class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache(maxsize=None)
        def LCS(count, index):
            
            if len(text1) == count or len(text2) == index:
                return 0

            if text1[count] == text2[index]:
                return 1 + LCS(count + 1, index + 1)
            else:
                return max(LCS(count, index + 1), LCS(count + 1, index))
            
        return LCS(0, 0)