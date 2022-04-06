class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        #send to A
       
        s=0
        n=len(costs)//2
        costs.sort(key= lambda t:t[1]-t[0])
        for i in range(n):
            s=s+costs[i][1]
        for i in range(n,n*2):
            s=s+costs[i][0]
        
        return s