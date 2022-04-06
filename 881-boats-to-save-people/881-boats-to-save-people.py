class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        i=0
        j=len(people)-1
        people.sort()
        b=0
        while i<j:
            if people[i]+people[j]<=limit:
                b+=1
                i+=1
                j-=1
            else:
                b+=1
                j-=1
        print(i,j,b+1,people)
        return b+1 if i==j else b