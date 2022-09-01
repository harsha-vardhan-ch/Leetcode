class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s=s+t
        d=set()
        for i in s:
            if i not in d:
                d.add(i)
            else:
                d.remove(i)
        
        return d.pop()
        