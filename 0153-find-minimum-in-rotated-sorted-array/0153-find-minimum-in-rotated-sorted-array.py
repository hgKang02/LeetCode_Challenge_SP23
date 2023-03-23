class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        min_val = nums[0]
        right = len(nums) - 1
        left = 0
        if nums[left] < nums[right]:
            return nums[left]
        while left < right:
            if left == right:
                return nums[left]
            if nums[left] < nums[left + 1]:
                left += 1
            elif nums[left] > nums[left + 1]:
                min_val = nums[left + 1]
                break
            if nums[right] > nums[right - 1]:
                right -= 1
            elif nums[right] < nums[right - 1]:
                min_val = nums[right]
                break
            # if left == len(nums) or nums[left + 1] < nums[left]:
            #     min_val = nums[left + 1]
            #     break
            # if right == 0 or nums[right - 1] > nums[right]:
            #     min_val = nums[right]
            #     break
                
        return min_val
        
            