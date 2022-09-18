class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # return sorted(citations)[len(citations)//2]
        r=sorted(citations,reverse=True)
        for i in range(len(r)-1,-1,-1):
            if r[i]>i:
                return i+1
        return 0