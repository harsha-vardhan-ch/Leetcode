class Solution:
    def judgeCircle(self, moves: str) -> bool:
        def check(x,y):
            for i in ar:
                # print(i[0],i[1],x,y)
                if x==i[0] and y==i[1] and x==0 and y==0:
                    return True
            return False
        x=0
        y=0
        ar=[(0,0)]
        for i in moves:
            if i == 'U':
                y+=1
            elif i=='R':
                x+=1
            elif i=='L':
                x-=1  
            elif i=='D':
                y-=1
            # print(x,y)
            ar.append((x,y)) 
        # print(ar[-1][0])
        if ar[-1][0]==0 and ar[-1][1]==0:
            return True
            
        return False
        