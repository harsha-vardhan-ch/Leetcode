class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        res=[]
        c=0
        for i in range(len(nums)-1):
            if nums[i+1]<=nums[i]:
                res.append(c+1)
                c=0
            else:
                c+=1
        # print(res)
        res.append(c+1)
        return max(res)