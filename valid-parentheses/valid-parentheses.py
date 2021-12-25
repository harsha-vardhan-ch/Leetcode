class Solution:
    def isValid(self, s: str) -> bool:
        sta=[]
        for i in s:
            if i=='(' or i=='[' or i=='{':
                sta.append(i)
            elif i==')' and len(sta)>0 and sta[len(sta)-1]=='(':
                sta.pop()
            elif i==']' and len(sta)>0 and sta[len(sta)-1]=='[':
                sta.pop()
            elif i=='}' and len(sta)>0 and sta[len(sta)-1]=='{':
                sta.pop()
            else:
                return False
        if len(sta)==0:
            return True
                
                
                
        