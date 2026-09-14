class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        total_water = 0
        left_max = height[left]
        right_max = height[right]

        while left < right:
            if left_max < right_max:
                total_water += left_max - height[left]
                left += 1
                left_max = max(left_max,height[left]) 
            if right_max <= left_max:
                total_water += right_max - height[right]
                right -= 1
                right_max = max(right_max,height[right]) 

        return total_water 