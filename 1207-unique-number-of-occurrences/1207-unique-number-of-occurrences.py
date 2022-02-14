class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d=Counter(arr)
        s=set()
        l=[]
        for k,v in d.items():
            l.append(v)
            s.add(v)
        if len(s)-len(l)==0:
            return True
        return False
        
