class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        l=0
        r=0
        for i in s:
            if i=='(':
                r=r+1
            elif i==')' and r==0:
                l=l+1
            else:
                r=r-1
        #print(l+r)
        return l+r
        