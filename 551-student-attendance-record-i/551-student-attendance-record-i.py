class Solution:
    def checkRecord(self, s: str) -> bool:
        ab=0
        if s=='AA':
            return False
        for i in range(len(s)-2):
            # print(i)
            if ab == 2:
                return False
            elif s[i]=='L' and s[i+1]=='L' and s[i+2]=="L":
                return False
            elif s[i]=='A':
                ab+=1
        if ab==2:
            return False
        return True