class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        s=0
        e=len(nums)-1
        r=[0]*len(nums)
        n=e
        for i in range(len(nums)):
            f=nums[s]*nums[s]
            k=nums[n]*nums[n]
            if f>k:
                r[e]=f
                s+=1
            else:
                r[e]=k
                n=n-1
            e=e-1
            #print(r)
        return r