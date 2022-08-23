import heapq
class KthLargest:
    nums=[]
    k=0
    res=[]
    def __init__(self, k: int, nums: List[int]):
        self.nums=nums
        heapq.heapify(self.nums)
        self.k=k

    def add(self, val: int) -> int:
        '''
        App 1
        
        heapq.heappush(self.nums,val)
        return heapq.nlargest(self.k,self.nums)[-1]
        '''
        '''
        App 2
        '''
        heapq.heappush(self.nums, val)
        while len(self.nums) > self.k: 
            # print(self.nums)
            heapq.heappop(self.nums)
        return self.nums[0] # the root element
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)