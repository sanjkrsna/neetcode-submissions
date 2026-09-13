class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = prices[0]
        res = 0
        for price in prices:
            if price < l:
                l = price
            res = max(res,price - l)
        return res

        