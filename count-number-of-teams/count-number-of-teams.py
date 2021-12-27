class Solution:
    def numTeams(self, rating: List[int]) -> int:
        c=0
        for i,v in enumerate(rating):
            leftsmco=0
            leftgtco=0
            rismco=0
            rigtco=0
            for j in rating[:i]:
                if j<v:
                    leftsmco+=1
                elif j>v:
                    leftgtco+=1
            for j in rating[i+1:]:
                if v>j:
                    rismco+=1
                elif v<j:
                    rigtco+=1
            #print(leftsmco,rigtco,leftgtco,rismco)
            c=c+ leftsmco*rigtco + leftgtco*rismco
        return c