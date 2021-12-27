class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        cur=0
        prev=0
        for i in nums:
            prev,cur=cur,max(prev+i,cur)
        return cur
    '''
        for i in nums:
            prev=cur
            if prev+i > cur:
                cur = prev+i
        return cur'''