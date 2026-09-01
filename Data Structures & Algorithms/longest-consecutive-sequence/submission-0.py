class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        m = 0
        for i in s:
            if i -1 not in s:
                length = 0
                while (i + length) in s:
                    length +=1
                    if length > m:
                        m = length
        return m


        