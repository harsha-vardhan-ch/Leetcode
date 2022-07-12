class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        news=[]
        for i in nums:
            if i%original == 0:
                news.append(i)
        
        while original in news:
            original*=2
        return original