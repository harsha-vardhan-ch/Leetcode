class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        k=len(nums)
        while k>=2:
            for i in range(k-1):
                t=nums[i]+nums[i+1]
                if t>9:
                    t = t%10
                nums[i]=t
            k-=1
        return nums[0]