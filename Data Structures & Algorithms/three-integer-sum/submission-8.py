class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            l,r = i+1, len(nums)-1
            while l < r:
                targetSum = nums[i]+nums[l]+nums[r]
                if targetSum > 0:
                    r -= 1
                elif targetSum < 0:
                    l += 1
                elif targetSum == 0 and i != l and i != r and l != r:
                    result.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
        new_res = []
        for elem in result:
            if elem not in new_res:
                new_res.append(elem)
        return new_res
        