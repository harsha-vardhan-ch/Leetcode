class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        d=set()
        for mail in emails:
            r=''
            i=0
            at=0
            while i<len(mail):
                # print('h',mail[i])
                if at==1:
                    
                    r=r+mail[i:]
                    break
                elif mail[i]=='+':
                    t=mail.find('@')-i
                    i=i+t
                    at=1
                elif mail[i]=='@':
                    at=1
                elif mail[i]!='.':
                    r=r+mail[i]
                    i+=1
                
                else:
                    i+=1
            d.add(r)
        print(d)
        return len(d)
                    