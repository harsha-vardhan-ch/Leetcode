class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        App 1
        T.C - O(N^2) = N(N-1)/2
        S.C - O(1)
        '''
#         max_profit = 0
#         for i in range(len(prices) - 1):
#             for j in range(i + 1, len(prices)):
#                 profit = prices[j] - prices[i]
#                 if profit > max_profit:
#                     max_profit = profit
                    
#         return max_profit
    
        '''
        App 2
        T.C - O(n)
        S.c -O(1)
        '''
        minprice=float('inf')
        maxpro=0
        for i in range(len(prices)):
            if prices[i]<minprice:
                minprice=prices[i]
            if prices[i]-minprice>maxpro:
                maxpro=prices[i]-minprice
        return maxpro
        
    