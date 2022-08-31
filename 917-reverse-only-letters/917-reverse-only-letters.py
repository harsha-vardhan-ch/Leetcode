class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        i=0
        n=len(s)-1
        s=list(s)
        while i<n:
            if not s[i].isalpha():
                i+=1
            elif not s[n].isalpha():
                n-=1
            else:
                s[i],s[n]=s[n],s[i]
                i+=1
                n-=1
        return "".join(s)
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # S, i, j = list(S), 0, len(S) - 1
        # while i < j:
        #     if not S[i].isalpha():
        #         i += 1
        #     elif not S[j].isalpha():
        #         j -= 1
        #     else:
        #         S[i], S[j] = S[j], S[i]
        #         i, j = i + 1, j - 1
        # return "".join(S)