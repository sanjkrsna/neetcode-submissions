class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = {}
        for st in s:
            if st in freq_s:
                freq_s[st] += 1
            else:
                freq_s[st] = 1
        
        for tt in t:
            if tt in freq_s:
                freq_s[tt] -= 1
            else:
                return False
                
        for count in freq_s.values():
            if count != 0:
                return False
        return True