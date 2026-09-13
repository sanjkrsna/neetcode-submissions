class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        sequence_len = 1
        largest_sequence = 1
        set_num = list(set(nums))
        set_num.sort()
        print(set_num)
        for i in range(1,len(set_num)):
            if set_num[i]-set_num[i-1] == 1:
                sequence_len += 1
                largest_sequence = max(sequence_len,largest_sequence)
            else:
                sequence_len = 1
        
        return largest_sequence
        