class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashMap = {}
        longest = 0
        for num in nums:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1
        
        for key in hashMap.keys():
            if key - 1 not in hashMap:
                length = 1
                while (key+length) in hashMap:
                    length += 1
                longest = max(length,longest)
        return longest
        
        
        