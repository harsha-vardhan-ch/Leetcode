class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        
        '''
        App 1
        T.C - O(n^2)
        S.C - O(n)
        '''
        w1=[]
        w2=[]
        for i in range(len(words)):
            if words[i]==word1:
                w1.append(i)
            if words[i]==word2:
                w2.append(i)
        res=len(words)
        for i in range(len(w1)):
            for j in range(len(w2)):
                if abs(w1[i]-w2[j])<res:
                    res=abs(w1[i]-w2[j])
        # return abs(min(w1)-min(w2))
        return res
        '''
        App 2
        T.C - O(n)
        S.C = O(1)
        '''
#         size = len(words)
#         w1,w2=size,size
#         ans = size

#         for i in range(size):
#             if words[i] == word1:
#                 w1 = i
#                 ans = min(ans, abs(w1-w2))
#             elif words[i] == word2:
#                 index2 = i
#                 ans = min(ans, abs(w1-w2))
#         return ans