class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPurchase = prices[0]
        for i in range(1, len(prices)):		
            maxProfit = max(maxProfit, prices[i] - minPurchase)
            print(minPurchase,'    f')
            minPurchase = min(minPurchase, prices[i])
            print(minPurchase)
        return maxProfit