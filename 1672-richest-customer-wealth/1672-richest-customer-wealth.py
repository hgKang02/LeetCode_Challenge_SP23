class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for i in accounts:
            cur_wealth = 0
            for j in i:
                cur_wealth += j
            if cur_wealth > max_wealth:
                max_wealth = cur_wealth
        
        return max_wealth