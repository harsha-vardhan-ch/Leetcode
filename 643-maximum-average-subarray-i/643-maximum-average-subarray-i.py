class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        c=sum(nums[:k])
        m=c/k
        for i in range(k,len(nums)):
            c=c+nums[i]-nums[i-k]
            if c/k > m:
                m=c/k
        return m
        