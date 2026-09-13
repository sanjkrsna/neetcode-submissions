class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashMap = {'}':'{',']':'[',')':'('}
        for c in s:
            if c not in hashMap:
                stack.append(c)
                continue
            if not stack or stack[-1] != hashMap[c]:
                return False
            stack.pop()

        return not stack
        
            
        