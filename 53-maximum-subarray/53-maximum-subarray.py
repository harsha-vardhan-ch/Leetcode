class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        msum=nums[0]
        curr=0
        for i in nums:
            if curr<0:
                curr=0
            curr=curr+i
            if curr>msum:
                msum=curr
        return msum