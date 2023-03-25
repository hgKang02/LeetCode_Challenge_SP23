class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        num = 0
        for i in nums:
            if i == num:
                num += 1
            else:
                return num
        return len(nums)