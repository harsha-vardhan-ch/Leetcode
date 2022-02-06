class Solution:
    def decodeString(self, s: str) -> str:
        '''
        fr=''
        num=[]
        stack=[]
        for i in range(len(s)):
            if s[i]=='[':
                stack.append(s[i])
            elif s[i]==']':
                j=len(stack)-1
                r=''
                while j>=0 and stack[j]!='[':
                    r=r+stack[j]
                    stack.pop()
                    j=j-1
                stack.pop()
                r=r[::-1]*num[-1]
                fr=fr+r
                del num[-1]
            elif s[i].isdigit():
                nu=s[i:].index('[')+i
                num.append(int(s[i:nu]))
            else:
                stack.append(s[i])
        return fr
                
        '''
        stack = []; curNum = 0; curString = ''
        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num*curString
            elif c.isdigit():
                curNum = curNum*10 + int(c)
            else:
                curString += c
        return curString