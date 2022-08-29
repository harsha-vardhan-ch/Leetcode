class Solution:
    def isPathCrossing(self, path: str) -> bool:
        def check(x,y):
            for i in ar:
                # print(i[0],i[1],x,y)
                if x==i[0] and y==i[1]:
                    return True
            return False
        x=0
        y=0
        ar=[(0,0)]
        for i in path:
            if i == 'N':
                y+=1
            elif i=='E':
                x+=1
            elif i=='W':
                x-=1  
            elif i=='S':
                y-=1
            # print(x,y)
            if check(x,y):
                return True
            ar.append((x,y)) 
            
            
        # print(ar)
        return False
        