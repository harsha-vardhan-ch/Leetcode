class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        sing = ['1','0','8']
        if len(num)<2:
            if num in sing:
                return True
            return False
        i=0
        j=len(num)-1
        d = { '0':'0', '6':'9', '8':'8', '9':'6', '1':'1'}
        while i<j:
            if num[i] not in d:
                return False
            if d[num[i]] == num[j]:
                i+=1
                j-=1
            else:
                return False
        if num[i]==num[j] and num[i] in sing:
            return True
        elif num[i]==num[j] and num[i] not in sing:
            return False
        return True
            