class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # res=[i for i in range(2**k)]
        # # print(res)
        # c=0
        # if k<2:
        #     if '0' in s and '1' in s:
        #         return True
        #     return False
        # i=0
        # k=0
        # while i<len(s)-1:
        #     # print(k)
        #     num = 2*int(s[i]) + int(s[i+1])
        #     # print(num,c,len(res))
        #     if num in res:
        #         c+=1
        #     if c==len(res):
        #         return True
        #     i+=1
        # # print(c,res)
        # # if c==2**k:
        # #     return True
        # return False
        
        codes = set()
        for i in range(len(s) - k + 1):
            codes.add(s[i:i+k])
        return len(codes) == 2 ** k