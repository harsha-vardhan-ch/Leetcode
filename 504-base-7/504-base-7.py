class Solution:
    def convertToBase7(self, num: int) -> str:
        # print(int(num,7))
        if num==0:
            return "0"
        res = ''
        r=1
        c=0
        if num<0:
            num=num*-1
            c=1
        while num!=0:
            r=num%7
            res=res+str(r)
            num=num//7
        if c==1:
            res=res+'-'
        return res[::-1]