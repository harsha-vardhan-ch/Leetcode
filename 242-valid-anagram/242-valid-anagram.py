class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        App 1
        
        By using dictionaries
        make s dict
        make t dict 
        compare both dicts
        
        T.C - O( len s + len t)
        S.C - same
        
        '''
        s_dic = {}
        t_dic = {}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            # if i not in s_dic:
            #     s_dic[i]=1
            #     t_dic[i]=1
            # else:
            #     s_dic[i]+=1
            #     t_dic[i]+=1
            s_dic[s[i]] = 1+ s_dic.get(s[i],0)
            t_dic[t[i]] = 1+ t_dic.get(t[i],0)
        print(s_dic,t_dic)
        for i in s_dic:
            # print(i)
            if s_dic[i]!=t_dic.get(i,0):
                return False
        return True
    
    '''
    App 2
    
    return Counter(s) == Counter(t) 
    T.C, S.C same as App1
    
    
    App 3
    
    Sort Strings and compare 
    
    return sorted(s)==sorted(t)
    
    T.C - O( nlogn )
    S.C - O ( 1 ) ( Assumption )
    
    '''
        