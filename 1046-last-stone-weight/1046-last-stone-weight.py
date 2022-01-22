class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones)==1:
            return stones[0]
        n=len(stones)
        s=stones
        while n>=2:
            s=sorted(s)
            a=s[-1]
            b=s[-2]
            del s[-1]
            del s[-1] 
            if a<b:
                s.append(b-a)
            elif a>b:
                s.append(a-b)
            n=len(s)
        if len(s)==0:
            return 0
        return s[0]