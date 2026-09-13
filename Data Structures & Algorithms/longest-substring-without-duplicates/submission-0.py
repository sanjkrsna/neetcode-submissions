class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        n = len(s)
        
        for i in range(n):
            visited = [False] * 256  # Since there are 256 ASCII characters
            length = 0

            for j in range(i, n):
                if visited[ord(s[j])]:  # If character s[j] is already seen, break
                    break
                visited[ord(s[j])] = True  # Mark the character as seen
                length += 1  # Increase the length of the substring
                
            max_len = max(max_len, length)  # Update max_len with the maximum length

        return max_len

            
            

        