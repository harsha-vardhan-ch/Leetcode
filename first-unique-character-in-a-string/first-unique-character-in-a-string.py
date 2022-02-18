class Solution:
    def firstUniqChar(self, s: str) -> int:
        d={}
        #print(Counter(s))
        r=Counter(s)
        for i in r:
            if r[i]==1:
                return s.index(i)
        return -1
            