class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        left = 0
        right = len(x) - 1
        while left <= right:
            if x[left] != x[right]:
                return False
            left += 1
            if left == right:
                break
            right -= 1
        # for i in range(len(string)):
        #     if i <= len(string) // 2:
        #         arr.append(string[i])
        #     else:
        #         arr2.append(string[i])
        # for i in range(1, len(string) // 2):
        #     if arr[i] != arr2[len(string) - i]:
        #         return False
        return True
