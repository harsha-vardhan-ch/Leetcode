class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        r=[0 for i in range(n)]
        m=-1
        for i in range(n-1,-1,-1):
            r[i]=m
            m=max(arr[i],m)
        return r
    
    '''
        
        mx=-1
        for i in range(len(A) - 1, -1, -1):
            A[i], mx = mx, max(mx, A[i])
        return A
    '''