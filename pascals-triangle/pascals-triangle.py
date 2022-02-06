class Solution:
    def generate(self, n: int) -> List[List[int]]:
        r=[[0],[1]]
        if n>1:
            r.append([1,1])
        if n==2:
            del r[0]
            return r
        for i in range(3,n+1):
            t=[1]
            for j in range(1,i-2+1):
                t.append(r[i-1][j-1]+r[i-1][j])
            t.append(1)
            r.append(t)
        del r[0]
        return r