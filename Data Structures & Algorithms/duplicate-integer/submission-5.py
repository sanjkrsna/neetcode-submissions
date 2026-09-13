class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasDuplicate = set()
        for num in nums:
            if num not in hasDuplicate:
                hasDuplicate.add(num)
            else:
                return True
        return False
        