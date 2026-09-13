class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        for n in nums:
            if n in dict1:
                dict1[n] += 1
            else:
                dict1[n] = 1

        dict2 = {}
        for n,c in dict1.items():
            if c not in dict2:
                dict2[c] = []
            dict2[c].append(n)

        result = []
        for i in range(len(nums),0,-1):
            if i in dict2:
                result.extend(dict2[i])
            if len(result) == k:
                return result
        
        