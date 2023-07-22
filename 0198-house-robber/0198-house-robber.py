class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        else:
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = nums[1]
            dp[2] = max(nums[2] + dp[0], dp[1])
            # if len(nums) % 2 == 0:
            #     dp[2] = max(nums[2] + dp[0], dp[1])
            #     for i in range(3, len(nums)):
            #         dp[i] = max(nums[i] + dp[i - 2], dp[i -1], dp[ i - 3] + nums[i])
            # else:
            #     for i in range(2, len(nums)):
            #         dp[i] = max(nums[i] + dp[i - 2], dp[i -1])
            # dp[2] = max(nums[2] + dp[0], dp[1])
            for i in range(3, len(nums)):
                dp[i] = max(nums[i] + dp[i - 2], dp[i -1], dp[ i - 3] + nums[i])
            return dp[len(dp) - 1]