class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        s=1
        while s:
            r=s
            for i in nums:
                r=r+i
                if r<1:
                    break
            if r>=1:
                return s
            s=s+1