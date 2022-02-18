class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        print('0'<'1')
        def newstr(s):
            v_n=s.split(".")
            for i in range(len(v_n)):
                if len(v_n[i])>1:
                    v_n[i]=v_n[i].lstrip("0")
                    if len(v_n[i])==0:
                        v_n[i]='0'
            return v_n
        
        v2_n=newstr(v2)
        v1_n=newstr(v1)
        print(v1_n,v2_n)
        d=abs(len(v2_n)-len(v1_n))
        if len(v1_n)<len(v2_n):
            for i in range(d):
                v1_n.append('0')
        else:
            for i in range(d):
                v2_n.append('0')
        i=0
        j=0
        #print(v1_n,v2_n)
        while i<len(v1_n) and j<len(v2_n):
            if int(v1_n[i])<int(v2_n[j]):
                return -1
            elif int(v1_n[i])>int(v2_n[j]):
                return 1
            i+=1
            j+=1
        #print(i,j)
        return 0
        