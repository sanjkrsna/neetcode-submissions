class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod = 1
        left_prefix_prod = []
        for i in range(len(nums)):
            left_prefix_prod.append(left_prod)
            left_prod = left_prod*nums[i]

        right_prod = 1
        right_prefix_prod = [None]*len(nums)

        for j in range(len(nums)-1,-1,-1):
            right_prefix_prod[j] = right_prod
            right_prod = right_prod*nums[j]

        ans = []
        for i in range(len(nums)):
            ans.append(left_prefix_prod[i]*right_prefix_prod[i])

        
        return ans