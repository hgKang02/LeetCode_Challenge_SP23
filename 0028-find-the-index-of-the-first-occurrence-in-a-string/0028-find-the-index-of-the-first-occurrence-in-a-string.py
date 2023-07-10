class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        end_point = len(haystack) - len(needle) + 1
        
        
        # for i in range(end_point):
        #     for j in range(len(needle)):
        #         if haystack[i + j] != needle[j]:
        #             break
        #         elif j == len(needle) - 1:
        #             return i
        for i in range(end_point):
            for j in range(len(needle)):
                if haystack[i: i + j + 1] == needle:
                    return i

        return -1
            
            
        