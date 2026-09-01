class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cSet = set()
        left = 0
        right = 0
        m = 0
        while right < len(s):
            while s[right] in cSet:
                cSet.discard(s[left])
                left +=1
            cSet.add(s[right])
            right +=1
            m = max(m, right-left)

        return m
