class Solution:
    def isValid(self, s: str) -> bool:
        agg = []
        pairs = {'}': '{', ']':'[', ')':'('}
        for c in s:
            if c in pairs:
                if agg and pairs[c] == agg[-1]:
                    print(f"found pair for {c}")
                    agg.pop()
                    print(agg)
                else:
                    return False
            else:
                print(f"new start {c}")
                agg.append(c)
        return True if not agg else False

        