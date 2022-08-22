import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ny=[]
        for i in nums:
            heapq.heappush(ny,-i)
        for j in range(k):
            res=-heapq.heappop(ny)
        return res
            