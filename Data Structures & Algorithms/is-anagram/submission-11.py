class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) < len(t) or len(t) < len(s):
            return False
        anagramDict = {}
        for chars in s:
            if chars not in anagramDict:
                anagramDict[chars]=1
            else:
                anagramDict[chars]+=1

        
        for chars in t:
            if chars in anagramDict:
                anagramDict[chars]-=1
            else:
                return False

            
        for key,value in anagramDict.items():
            if value != 0:
                return False
        
        return True
        