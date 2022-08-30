class Solution:
    def removeDuplicates(self, s: str) -> str:
        '''
        App 1
        Time limit exceeded
        '''
        '''
        n=len(s)
        arr=[i for i in s]
        t=s
        i=0
        while i!=n-1 and n>=2:
            # print(i,arr)
            if arr[i]==arr[i+1]:
                del arr[i]
                del arr[i]
                n=len(arr)
                i=0
            else:
                i+=1
        return "".join(arr)
        '''
        '''
        App 2 
        Stack
        T.C - O(n)
        S.C - O(n-d) , d=length of duplicates
        '''
        res=[s[0]]
        for i in range(1,len(s)):
            # print(res,i,s[i])
            if len(res)>0:
                if res[-1]==s[i]:
                    # print(res,i,s[i])
                    del res[-1]
                else:
                    res.append(s[i])
            else:
                res.append(s[i])
        return "".join(res)
            