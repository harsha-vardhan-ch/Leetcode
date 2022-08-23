from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # print(Counter(nums))
        res=[]
        for k, v in Counter(nums).most_common(k):
            # print(k,v)
            res.append(k)
        return res