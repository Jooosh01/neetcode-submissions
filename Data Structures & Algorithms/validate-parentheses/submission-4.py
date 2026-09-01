class Solution:
    def isValid(self, s: str) -> bool:
        agg = []
        pairs = {'}': '{', ']':'[', ')':'('}
        for c in s:
            if c in pairs:
                if len(agg) > 0 and pairs[c] == agg[-1]:
                    agg.pop()
                else:
                    return False
            else:
                agg.append(c)
        return True if not agg else False

        