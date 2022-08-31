class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        '''
        App 1
        '''
        # r=0
        # for word in words:
        #     for i in word:
        #         if i not in chars:
        #             break
        #     if i==word[-1]:
        #         r=r+len(word)
        # return r
        
        '''
        App 2
        '''
        r=0
        cc = collections.Counter(chars)
        for word in words:
            wc = collections.Counter(word)
            for c in wc:
                if wc[c] > cc[c]:
                    break
            else:
                r += len(word)
        return r