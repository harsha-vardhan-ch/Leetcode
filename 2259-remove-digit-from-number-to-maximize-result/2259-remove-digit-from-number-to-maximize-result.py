class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        res=[]
        for i in range(len(number)):
            # print(number[i],' ',i,' ',digit)
            if number[i] == digit:
                res.append(number[:i]+number[i+1:])
        return max(res)