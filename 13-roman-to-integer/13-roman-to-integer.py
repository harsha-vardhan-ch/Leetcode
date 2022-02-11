class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        r=0
        i=0
        while i<len(s)-1:
            if roman[s[i]]<roman[s[i+1]]:
                r=r+roman[s[i+1]] - roman[s[i]]
                i=i+1
            else:
                r=r+roman[s[i]]
            i+=1
        print(i)
        if i==len(s):
            return r
        else:
            return r+roman[s[i]]