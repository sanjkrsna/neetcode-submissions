class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = {}
        output = False
        for c in s:
            if c not in a:
                a[c] = 1
            else:
                a[c] += 1
        
        for c in t:
            if c in a:
                a[c] -= 1
            if c not in a:
                return False
        
        
        for key,value in a.items():
            if value == 0:
                output = True
            else:
                output = False
        
        return output