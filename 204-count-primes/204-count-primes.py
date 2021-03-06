class Solution:
    def countPrimes(self, n: int) -> int:
        '''
        if n<2:
            return 0
        
        c=0
        prm_array=[0]*n
        for i in range(2,int(math.sqrt(n))):
            if prm_array[i]==0:
                c+=1
                j=2
                while i*j<n:
                    prm_array[i*j]=1
                    j=j+1
        return c
        '''      
        not_prime = [0] * n
        count = 0
        for i in range(2, n):
            if not_prime[i]==0:
                count += 1
                for j in range(i*i,n,i):
                    not_prime[j] = 1
        #print not_prime
        return count
        
        