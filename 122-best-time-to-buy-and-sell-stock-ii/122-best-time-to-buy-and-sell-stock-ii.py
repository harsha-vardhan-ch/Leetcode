class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        App 2
        T.C - O(n)
        S.C - O(1)
        '''
        mpro=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                mpro+=prices[i]-prices[i-1]
        return mpro