class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        #send to A
        a=[]
        b=[]
        r=[]
        s=0
        n=len(costs)//2
        
        for cost in costs:
            a.append(cost[0])
            r.append(cost[1]-cost[0])
        print(r,costs)
        costs.sort(key= lambda t:t[1]-t[0])
        for i in range(n):
            s=s+costs[i][1]
            
        for i in range(n,len(costs)):
            s=s+costs[i][0]
        
        print(a,r[0:len(costs)//2],r,costs)
        
        return s