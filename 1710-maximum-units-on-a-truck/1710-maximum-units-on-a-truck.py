class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        t=truckSize
        c=0
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        for i in boxTypes:
            if i[0]<=t:
                t=t-i[0]
                c=c+ i[0]*i[1]
            else:
                c=c+ (t)*i[1]
                return c 
        return c
    