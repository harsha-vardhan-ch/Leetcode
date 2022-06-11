class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # for i in range(len(arr)):
        n=len(arr)
        i=0
        while i<n:
            if arr[i]==0:
                arr.insert(i,0)
                i+=1
                del arr[-1]
            i+=1
        