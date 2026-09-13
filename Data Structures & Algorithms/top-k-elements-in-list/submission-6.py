class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        bucket = [[] for _ in range(len(nums)+1)]

        for num in nums:
            if num in dict1:
                dict1[num] += 1
            else:
                dict1[num] = 1
        
        for n, c in dict1.items():
            bucket[c].append(n)
        
        result = []
        for i in range(len(bucket)-1,0,-1):
            for n in bucket[i]:
                result.append(n)
                if len(result) == k:
                    return result

        
        