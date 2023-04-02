class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        sol = set(nums)
        
        for num in sol:
            if num - 1 not in sol:
                curr_count = 1
                current = num
                
                while current + 1 in sol:
                    current += 1
                    curr_count += 1
                    
                count = max(count, curr_count)
        
        return count
            
            