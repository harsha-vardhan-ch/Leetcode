class Solution:
    def removeVowels(self, s: str) -> str:
        '''
        App 1
        Since, strings are immutable and creating them requires allocating new memory, this method is inefficient.
        '''
        # res=''
        # for i in s:
        #     if i not in "aeiou":
        #         res+=i
        # return res
        
        '''
        App 2
        Allocating memory only for final string. But, if i not in 'aeiou' taken O(5) lookup. 
        '''
        # res=[]
        # for i in s:
        #     if i not in "aeiou":
        #         res.append(i)
        # return "".join(res)
    
        '''
        App 3.
        
        Hashtable/hashset gives O(1) lookup.
        '''
        res=[]
        vowels=set('aeiou')
        for i in s:
            if i not in vowels:
                res.append(i)
        return "".join(res)
        