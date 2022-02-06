class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        r=[]
        
        nums = [0] + nums
        for i in range(len(nums)):
            index = abs(nums[i])
            nums[index] = -abs(nums[index])
        print(nums)
        return [i for i in range(len(nums)) if nums[i] > 0]
        
        
        # Method 1
        # sort the array and do
        
        #Method 2
        # initialize an empty array of size n with 0 
        
        