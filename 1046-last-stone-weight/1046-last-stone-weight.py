class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones)==1:
            return stones[0]
        n=len(stones)
        s=stones
        while n>=2:
            s=sorted(s)
            print(s)
            a=s[-1]
            b=s[-2]
            print(a,b,s)
            del s[-1]
            del s[-1] 
            if a<b:
                s.append(b-a)
            elif a>b:
                print(s)
                s.append(a-b)
            n=len(s)
        print(s)
        if len(s)==0:
            return 0
        return s[0]