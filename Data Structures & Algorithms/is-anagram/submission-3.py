class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        a = {}
        for c in s:
            if c not in a:
                a[c] = 1
            else:
                a[c] += 1
        
        for c in t:
            if c in a:
                a[c] -= 1
            else:
                return False
        
        
        for key,value in a.items():
            if value != 0:
                return False
            
        
        return True
