class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        minim = float('inf')
        while l <= r:
            m = l + (r-l)//2
            minim = min(minim,nums[m])
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1 
            
        return min(minim,nums[l])
        