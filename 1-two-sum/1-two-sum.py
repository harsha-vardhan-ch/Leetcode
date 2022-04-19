class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        App 2 
        
        T.C - O(n)
        S.C - O(n)
        
        '''
        d={}
        n=len(nums)
        for i in range(n):
            res=target-nums[i]
            if res in d:
                return [d[res],i]
            d[nums[i]]=i
            # print(d)
            
        '''
        App 1 - Bruteforce 
        
        T.C - O(n^2)
        S.C - O( 1 )

        '''