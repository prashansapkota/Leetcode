class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        water = 0
        max_vol = 0
        
        while left < right:
            water = min(height[left], height[right]) * (right - left)
            max_vol = max(max_vol, water)

            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return max_vol
        





