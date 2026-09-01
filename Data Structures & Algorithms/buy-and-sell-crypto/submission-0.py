class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        l = 0
        r = 1
        while r< len(prices):
            if prices[l] < prices[r]:
                diff = prices[r] - prices[l]
                if diff > mp: 
                    mp = diff
                r +=1
            else:
                l = r
                r = l+1
        return mp
        