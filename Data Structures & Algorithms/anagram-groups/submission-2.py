class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        sample_dict = {}
        for s in strs:
            sorted_str = "".join(sorted(s))
            if sorted_str in sample_dict:
                sample_dict[sorted_str].append(s)
            else:
                sample_dict[sorted_str] = [s]
        
        for i,val in sample_dict.items():
            ans.append(val)

        return ans

