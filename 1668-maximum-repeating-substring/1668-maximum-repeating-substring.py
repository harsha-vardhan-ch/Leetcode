class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        '''
        App 1 - Bruteforce
        '''
        # count = 0
        # while word * (count + 1) in sequence:
        #     count +=  1        
        # return count
    
        '''
        App 2 - Through binary search
        '''
        if word not in sequence:
            return 0

        left = 1
        right = len(sequence) // len(word)
        while left <= right:
            mid = (left + right) // 2
            if word * mid in sequence:
                left = mid + 1
            else:
                right = mid - 1 
                
        return left - 1
        