class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        r=n
        dp=[[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i==j:
                    dp[i][j]=1
        for j in range(1,n):
            for i in range(n-1):
            
                # print(i,j)
                if j-i==1:
                    if  s[i]==s[j]:
                        dp[i][j]=1
                        r+=1
                elif s[i]==s[j]:
                    if dp[i+1][j-1]==1:
                        dp[i][j]=1
                        r+=1
                        
        # print(dp)
                    
        return r