class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        '''
        Bruteforce
        T.C - O(n)
        S.C - 
        '''
        x=set(arr)
        c=0
        for i in range(1,len(arr)+k+1):
            if i not in x:
                c+=1 
            if c==k:
                return i
        return 0
            
        
        '''
        
        O(n)
        '''