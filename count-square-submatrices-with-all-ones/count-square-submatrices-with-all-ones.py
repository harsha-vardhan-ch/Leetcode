class Solution:
    def countSquares(self, m: List[List[int]]) -> int:
        r=len(m)
        c=len(m[0])
        #si=[0 for i in range(max(r,c))]
        hv=0
        for i in range(r):
            for j in range(c):
                if m[i][j] == 1:    
                    if i==0 or j==0:
                        hv += 1
                    else: #m[i-1][j-1] and m[i-1][j] and m[i][j-1]:
                        
                        m[i][j]+=min(m[i-1][j-1],m[i-1][j],m[i][j-1])
                        hv=hv+m[i][j]

                        
        
        return hv
        