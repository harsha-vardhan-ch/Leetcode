class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        s=''
        for i in nums:
            s=s+str(i) 
        print(s)
        a=list(s.split('0'))
        print(a)
        if len(a)==1:
            return len(a[0])
        maxlen=0
        for i in range(len(a)-1):
            curr=len(a[i]+a[i+1])+1
            if curr>maxlen:
                maxlen=curr
        return maxlen