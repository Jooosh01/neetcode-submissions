class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sd = [0]*26
        for i in range(len(s)):
            sind = ord(s[i]) - ord('a')
            tind = ord(t[i]) - ord('a')
            sd[sind] +=1
            sd[tind] -=1
        return all(x == 0 for x in sd)

            

        