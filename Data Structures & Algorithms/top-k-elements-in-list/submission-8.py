class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sampleDict = {}
        ans = []
        for num in nums:
            if num not in sampleDict:
                sampleDict[num] = 1
            else:
                sampleDict[num] += 1
            
        for i, val in sampleDict.items():
            ans.append(val)

        ans = sorted(sampleDict, key=sampleDict.get, reverse=True)[:k]

        return(ans)


        