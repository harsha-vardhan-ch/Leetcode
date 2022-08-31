class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d={}
        n=len(pattern)
        toy=s.split(" ")
        # print(toy)
        if len(pattern)!=len(toy):
            return False
        i=0
        while i<n:
            r=d.get(pattern[i],-1)
            if r==-1:
                d[pattern[i]]=toy[i]
            elif d[pattern[i]]!=toy[i]:
                # print(d,pattern[i],toy[i])
                return False
            i+=1
        # print(d,len(list(d.values())),len(d))
        if len(set(list(d.values())))!=len(d):
            return False
        
        return True
                