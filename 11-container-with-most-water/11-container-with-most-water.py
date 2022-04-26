class Solution:
    def maxArea(self, h: List[int]) -> int:
        '''
        M1
        
        Brute Force -
        T.C - O ( n2)
        
        
        '''
        '''
        area=0
        for i in range(len(h)):
            for j in range(i+1,len(h)):
                temp = ( j - i ) * min(h[i],h[j])
                area = max(temp,area)
        return area
    
        '''
        '''
        M2 
        
        T.C - O(n)
        
        '''
        area = 0
        l=0
        r=len(h)-1
        while l<r:
            temp = ( r - l ) * min(h[l],h[r])
            area = max(temp,area)
            if h[l]>h[r]:
                r-=1
            elif h[r]>=h[l]:
                l+=1
        return area
            
                
            
            