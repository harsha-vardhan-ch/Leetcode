class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        t=truckSize
        c=0
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        for i in boxTypes:
            print(i[0])
            if i[0]<=t:
                print(i[0], '    i[0]')
                t=t-i[0]
                c=c+ i[0]*i[1]
                print(c,'   c')
            else:
                print(i[0],i[1],t)
                c=c+ (t)*i[1]
                t=0
                print(c, 'cc',t)
                if t<=0:
                    return c
             
        return c
    