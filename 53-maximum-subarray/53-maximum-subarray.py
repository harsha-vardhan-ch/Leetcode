class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        msum=nums[0]
        csum=nums[0]
        for i in nums[1:]:
            if csum<0:
                csum=0
            csum=csum+i
            msum=max(msum,csum)
            
        return msum
            