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
            if t[i] not in td:
                td[t[i]] = 1
            else:
                td[t[i]] +=1
        for k in sd.keys():
            if k not in td:
                return False
            elif sd[k] != td[k]:
                return False
        return True

        