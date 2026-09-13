from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def multiply(arr: List[int], n: int, exclude_index: int) -> int:
            # Base case
            if n < 0:
                return 1
            
            # Skip the element at the exclude_index
            if n == exclude_index:
                return multiply(arr, n - 1, exclude_index)
            else:
                return arr[n] * multiply(arr, n - 1, exclude_index)
        
        n = len(nums)
        result = []
        
        i = 0
        while i < n:
            # Compute the product of all elements except nums[i]
            product = multiply(nums, n - 1, i)
            result.append(product)
            i += 1
        
        return result


