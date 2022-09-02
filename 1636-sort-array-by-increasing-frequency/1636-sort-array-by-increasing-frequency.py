class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
#         x=Counter(nums)
        
#         x=sorted(x.items(),key = lambda x: x[0], reverse=True)
#         x=sorted(x.items(),key=lambda pair: pair[1], reverse=False)
        
        x = Counter(nums).most_common()
        # print(x)
        x.sort(key = lambda a: a[0], reverse=True)
        # print(x)
        x.sort(key = lambda a: a[1])
        # print(x)
        
        r=[]
        for t in x:
            r=r+[t[0] for _ in range(t[1])]
        return r