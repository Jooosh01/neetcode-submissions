class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        l = 0
        r = 1
        while r< len(prices):
            if prices[r] < prices[l]:
                l=r
            else:
                diff = prices[r]-prices[l]
                mp = max(mp, diff)
            r +=1
        return mp
        