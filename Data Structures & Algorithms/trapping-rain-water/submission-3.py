class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0


        n = len(height)
        max_left = height[0]
        left_capacity = [0]*n
        left_capacity[0] = max_left
        total_water = 0
        for i in range(1,n):
            max_left = max(max_left,height[i])
            left_capacity[i] = max_left

        max_right = height[-1]
        right_capacity = [0]*n
        right_capacity[-1] = max_right
        for j in range(n-2,-1,-1):
            max_right = max(max_right,height[j])
            right_capacity[j] = max_right

        for i in range(n):
            total_water += min(right_capacity[i],left_capacity[i]) - height[i]

        return total_water



        