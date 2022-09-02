class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        '''
        App 1 - Bruteforce
        T.C - O(n^3)
        S.C - O(1)
        '''
        '''
        App 2 - Sort
        T.C - O(nlogn)
        S.C - O(logn) - space by sorting.
        '''
        nums.sort()
        return max(nums[-1]*nums[-2]*nums[-3],nums[0]*nums[1]*nums[-1])
        return max(large1 * large2 * large3, small1* small2 * large1)
        
        '''
        App 3
        Find large1, large2, large3, small1, small2 without sort
        T.C - O(n)
        S.C - O(1)
        '''
        