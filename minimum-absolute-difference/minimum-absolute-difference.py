class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        b=sorted(arr)
        r=[]
        m=abs(b[0]-b[1])
        x=[b[0],b[1]]
        r.append(x)
        for i in range(1,len(b)-1):
            h=abs(b[i]-b[i+1])
            if h==m:
                x=[b[i],b[i+1]]
                r.append(x)
            elif h<m:
                m=h
                r=[]
                x=[b[i],b[i+1]]
                r.append(x)
            
        return r
        