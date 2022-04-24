class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        M1 
        '''
#         temp=''
#         for i in s:
#             if i.isalnum():
#                 temp+=i.lower()
#         # print(temp)
#         return temp[::-1]==temp
    
        '''
        M 2
        '''
        l=0
        r=len(s)-1
        while l<r:
            while l<r and not s[l].isalnum():
                l+=1
            while r>l and not s[r].isalnum():
                r-=1
            if s[l].lower()!=s[r].lower():
                return False
            
            l+=1
            r-=1
        return True
    
        '''
        T.C - same
        Memory - Efficent that M1
        '''