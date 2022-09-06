class Solution:
    def isRobotBounded(self, ins: str) -> bool:
        def chgdir(face,inst):
            right={'W':'N','N':'E','E':'S','S':'W'}
            left={'W':'S','S':'E','E':'N','N':'W'}
            if inst=='L':
                return left[face]
            else:
                return right[face]
                    
        face='N'
        n=len(ins)
        if 'L' not in ins and 'R' not in ins:
            return False
        x=0
        y=0
        # ar=[(0,0)]
        i=0
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
                if i == (n-1) and ((x==0 and y==0) or face != 'N'):
                    return True
                # ar.append((x,y))         
            else:
                face = chgdir(face,ins[i])
                if i == (n-1) and ((x==0 and y==0) or face != 'N'):
                    return True
            i+=1
        return False
        