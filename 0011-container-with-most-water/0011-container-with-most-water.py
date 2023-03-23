class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        max_val = 0
        left = 0
        right = len(height) - 1
        while left < right:
            nextRight = right
            nextLeft = left
            area = (right - left) * min(height[left], height[right])
            if area > max_val:
                max_val = area
            if height[right] > height[left]:
                nextLeft = left + 1
            else:
                nextRight = right - 1
            if nextLeft == left and nextRight == right:
                break
            left = nextLeft
            right = nextRight
                
        return max_val