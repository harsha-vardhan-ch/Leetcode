class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        d={}
        arr2=sorted(arr)
        ind=0
        rank=0
        while ind<len(arr2):
            if d.get(arr2[ind],-1)<0:
                d[arr2[ind]]=rank
                rank+=1
            ind+=1
        '''
        for i in arr2:
        if i not in d:
            d[i]=rank
            rank+=1
        '''   
        res=[]
        for i in arr:
            res.append(d[i]+1)
        return res