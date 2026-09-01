class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sd = dict()
        td = dict()
        for i in range(len(s)):
            if s[i] not in sd:
                sd[s[i]] = 1
            else:
                sd[s[i]] +=1
            if t[i] in sd:
                sd[t[i]] -= 1
            else:
                sd[t[i]] = -1
        return all(sd[k] == 0 for k in sd.keys())
            

        