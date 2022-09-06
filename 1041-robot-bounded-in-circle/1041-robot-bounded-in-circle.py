class Solution:
    def isRobotBounded(self, ins: str) -> bool:
#         insu=''
#         for i in ins:
#             if i != 'G':
#                 insu+=i
#         if insu == "":
#             return False
#         if len(insu) == 1 and (insu == 'L' or insu=='R'):
#             return True
#         for i in range(len(insu)-1):
#             if (insu[i]=='L' and insu[i+1]=='L') or (insu[i]=='R' and insu[i+1]=='R'):
#                 return True
            
#         return False
        # def check(x,y):
        #     for i in ar:
        #         # print(i[0],i[1],x,y)
        #         if x==i[0] and y==i[1]:
        #             return True
        #     return False
        def chgdir(face,inst):
            right={'W':'N','N':'E','E':'S','S':'W'}
            left={'W':'S','S':'E','E':'N','N':'W'}
            if inst=='L':
                return left[face]
            else:
                return right[face]
                    
        face='N'
        n=len(ins)
        # h='L' not in instructions
        # v='R' not in instructions
        # print(h,v) 
        if 'L' not in ins and 'R' not in ins:
            return False
        x=0
        y=0
        ar=[(0,0)]
        i=0
        # suck=0
        while i<len(ins):
            
            
            if ins[i] == 'G':
                if face == 'N':
                    y+=1
                elif face=='E':
                    x+=1
                elif face=='W':
                    x-=1  
                elif face=='S':
                    y-=1
                # if check(x,y):
                #     suck=1
                if i == (n-1) and ((x==0 and y==0) or face != 'N'):
                    # print('hv')
                    return True
                ar.append((x,y))         
            else:
                face = chgdir(face,ins[i])
                if i == (n-1) and ((x==0 and y==0) or face != 'N'):
                    return True
            # print(x,y)
            # print(ins[i],ar,face)
            i+=1
            # if suck==0 and i==n:
            #     i=0
            
        # print(ar)
        return False
        