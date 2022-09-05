class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        
        dp=[[0] * n for _ in range(n)]
        res=[]
        for i in range(n):
            dp[i][i]=1
            res.append(s[i])
        
        for j in range(1,n):
            for i in range(n-1):
            
                # print(i,j)
                if j-i==1:
                    if  s[i]==s[j]:
                        dp[i][j]=1
                    
                        res.append(s[i:j+1])
                elif s[i]==s[j]:
                    if dp[i+1][j-1]==1:
                        dp[i][j]=1
                        
                        res.append(s[i:j+1])
        res.sort(key=len)
        print(res[-1])
        return res[-1]
        
        
        