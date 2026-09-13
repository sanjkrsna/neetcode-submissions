class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        a = {}

        for c in s:
            if c in a:
                a[c] += 1
            else:
                a[c] = 1
        
        for c in t:
            if c in a:
                a[c] -= 1

        for k,v in a.items():
            if v > 0:
                return False
        return True  