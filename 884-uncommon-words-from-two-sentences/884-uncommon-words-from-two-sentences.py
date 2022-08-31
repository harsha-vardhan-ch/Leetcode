class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        res=Counter(s1.split()+s2.split())
        res=sorted(res.items(), key=lambda pair: pair[1])
        r=[]
        for item in res:
            if item[1]==1:
                r.append(item[0])
        return r
# [('c', 7), ('a', 5), ('b', 3)]
