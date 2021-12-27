class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        n=len(nums)
        for i in range(n):
            res=target-nums[i]
            if res in d:
                return [d[res],i]
            d[nums[i]]=i