class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        c=0
        for word in words:
            ind = s.find(word)
            # print(ind)
            if ind == 0:
                c+=1
                
        return c
    
        # count=0
        # for word in words:
        #     if word==s[:len(word)]:
        #         count+=1
        # return count
            