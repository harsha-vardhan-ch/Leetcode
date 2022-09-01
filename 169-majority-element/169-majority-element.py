class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # return Counter(nums).most_common(1)[0][0]
    
        '''
        App 1

        Counter 

        T.C - O(n)
        S.C - O(n)
        '''

        '''
        App 2

        Sort and return middle lemeent
        T.C - O(nlogn)
        S.C - O(1)

        '''

        '''
        App 3

        Boyer moore voting algorithm
        T.C - O(n)
        S.C -O(1)

        '''
        can=0
        c=0
        for i in nums:
            if c==0:
                can=i
            if can!=i:
                c=c-1
            else:
                c=c+1
        return can
            
        