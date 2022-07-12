class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        # alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        i=97
        d={}
        d[" "]=" "
        for j in key:
            if j!=" " and j not in d:
                d[j]=chr(i)
                i+=1
            if len(d)==27:
                break
        res=""
        print(d)
        for i in message:
            res+=d[i]
        return res
