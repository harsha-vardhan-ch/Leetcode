class Solution:
    def judgeCircle(self, moves: str) -> bool:
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
            ar.append((x,y)) 
        if ar[-1][0]==0 and ar[-1][1]==0:
            return True   
        return False
        