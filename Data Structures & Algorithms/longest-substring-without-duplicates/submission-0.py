class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cSet = set()
        left = 0
        right = 0
        m = 0
        while right < len(s):
            if s[right] in cSet:
                while s[left] != s[right]:
                    cSet.discard(s[left])
                    left += 1
                left +=1
            else:
                cSet.add(s[right])
            
            right += 1
            m = max(m, right- left)
        return m
