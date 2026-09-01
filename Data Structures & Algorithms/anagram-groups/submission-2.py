class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        out = []
        def toArray (s:str) -> List[int]:
            temp = [0]*26
            for c in s:
                i = ord(c) - ord('a')
                temp[i] += 1
            return tuple(temp)
        for n in strs:
            a = toArray(n)
            if a in d:
                d[a].append(n)
            else:
                d[a] = [n]
        return list(d.values())

