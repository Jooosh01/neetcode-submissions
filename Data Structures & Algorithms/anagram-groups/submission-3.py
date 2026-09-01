class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def createCounts(n):
            agg = [0]*26
            for c in n:
                ind = ord(c) - ord('a')
                agg[ind] += 1
            return tuple(agg)
        d = dict()
        for s in strs:
            k = createCounts(s)
            if k in d:
                d[k].append(s)
            else:
                d[k] = [s]
        return list(d.values())

