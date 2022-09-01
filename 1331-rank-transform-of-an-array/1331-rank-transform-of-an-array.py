class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        d={}
        arr2=sorted(arr)
        ind=0
        v=0
        while ind<len(arr2):
            # print(ind,arr2[ind])
            if d.get(arr2[ind],-1)<0:
                d[arr2[ind]]=v
                v+=1
            ind+=1
        # print(d)
        res=[]
        for i in arr:
            res.append(d[i]+1)
        return res