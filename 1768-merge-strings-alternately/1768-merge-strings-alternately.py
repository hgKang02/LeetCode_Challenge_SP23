class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        first = True
        dif = abs(len(word1) - len(word2))
        if len(word1) - len(word2) < 0:
            first = False
        s = ""
        if first == True:
            for i in range(len(word1) - dif, len(word1)):
                s += word1[i]
        else:
            for i in range(len(word2) - dif, len(word2)):
                s += word2[i]
        result = ""
        for i in range(min(len(word1), len(word2))):
            result += word1[i]
            result += word2[i]
        
        return result + s
#         word = ""
#         length = max(len(word1),len(word2))
        
#         for i in range(length):
#             if i < len(word1):
#                 word += word1[i]
#             if i < len(word2):
#                 word += word2[i]
                
                
        #
        # first = False
        # if len(word1) >= len(word2):
        #     length = len(word2)
        #     first = True
        # else:
        #     length = len(word1)
        # word = "" 
        # for i in range(length):
        #     word += word1[i] + word2[i]
        # if first:
        #     for i in range(length, len(word1), 1):
        #         word += word1[i]
        # else:
        #     for i in range(length, len(word2), 1):
        #         word += word2[i]
        # return word
        