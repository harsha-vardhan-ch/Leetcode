class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        # w1c=-1
        # w2c=-1
        # for i in range(len(words)):
        #     if words[i]==word1 and w1c==-1:
        #         w1c=i
        #     if words[i]==word1 and w1c>-1:
        #         # second match
        #         if abs(i-w2c)<abs(w1c-w2c):
        #     elif words[i]==word2 and w2c==-1:
        #         w2c=i
        #     if w1c > -1 and w2c > -1:
        #         return abs(w1c-w2c)
        # return 0
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
        