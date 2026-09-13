class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i in range(len(nums)):
            prevMap[nums[i]] = i
        
        for i in range(len(nums)):
            req = target - nums[i]
            if req in prevMap and prevMap[req] != i:
                return [i,prevMap[req]]
            
        