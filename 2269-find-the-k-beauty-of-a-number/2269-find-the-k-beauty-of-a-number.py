class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        numString =str(num)
        count=0
        for i in range(0,len(numString)-k+1):
            x=int(numString[i:i+k])
            # if x and num%x==0:
            if x>0 and num%x==0:
                count+=1
        return count