class Solution:
    def check(self,temp):
        if temp==temp[::-1]:
            return True
        return False
    def validPalindrome(self, s: str) -> bool:
#         i=0
#         j=len(s)-1
#         while i<j:
            
#             if s[i]!=s[j]:
#                 return False
#             i+=1
#             j-=1
#         print(i,j)
#         if i==j:
#             return True
        c=0
        j=len(s)-1
        i=0
        while i<j:
            if s[i]!=s[j]:
                return (self.check(s[i+1:j+1]) or (self.check(s[i:j])))
            i+=1
            j-=1
        return True
                
        