class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sd = [0]*26
        for i in range(len(s)):
            sd[ord(s[i]) - ord('a')] +=1
            sd[ord(t[i]) - ord('a')] -=1
        return all(x == 0 for x in sd)

            

        