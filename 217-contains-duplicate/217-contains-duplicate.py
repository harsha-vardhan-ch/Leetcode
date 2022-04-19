class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        b=sorted(nums)
        n=len(b)
        for i in range(n-1):
            if b[i]==b[i+1]:
                return True
            
        return False
        
        '''
        App 1
        
        one by one checking 
        
        T.C - O(n ^ 2)
        S.C - O( 1 )
        
        
        App2 
        
        Sort and check 
        
        T.C - O(nlogn)
        S.C - O( 1 )
        
        App3
        
        use a set to add elements and check 
        
        T.C - O( n )
        S.C - O( n )
        
        a = set()
        for i in nums:
            if i in a:
                return False
            a.add(i)
        return False
        
        App 4
        
        if len(set(nums))!=len(nums):
            return False
        return True
        
        '''
        