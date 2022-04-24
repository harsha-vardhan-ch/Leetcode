class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        M1 
        
        T.C - O(n 2)
        
        
        for i in range(len(numbers)-1):
            for j in range(i+1,len(numbers)):
                if numbers[i]+numbers[j]==target:
                    return [i+1,j+1]
                elif numbers[i]+numbers[j]>target:
                    break
        
            
        '''
        '''
        M 2
        
        T.C - O(n)
        '''
        
        l, r = 0, len(numbers)-1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            elif s < target:
                l += 1
            else:
                r -= 1
        