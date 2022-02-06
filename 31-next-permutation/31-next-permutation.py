class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
        """
        n=len(nums)
        i=n-1
        
        while i>0 and nums[i]<=nums[i-1]:
            i-=1
        
        if i==0:
            nums.reverse()
            return 
        
        i=i-1
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        
        (nums[i],nums[j])=(nums[j],nums[i])
        
        nums[i+1:]=nums[n-1:i:-1]