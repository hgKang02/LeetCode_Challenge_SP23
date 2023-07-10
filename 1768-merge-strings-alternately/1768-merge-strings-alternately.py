class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word = ""
        length = max(len(word1),len(word2))
        
        for i in range(length):
            if i < len(word1):
                word += word1[i]
            if i < len(word2):
                word += word2[i]
        
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
        return word
        