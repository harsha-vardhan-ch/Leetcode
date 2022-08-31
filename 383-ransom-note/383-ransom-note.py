class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        '''
        App 1
        m = len(magazie)
        n=len(ransom)
        T.C - O(m.n)
        S.C - O(m)
        '''
        # for i in ransomNote:
        #     r=magazine.find(i)
        #     if r<0:
        #         return False
        #     else:
        #         magazine=magazine[:r]+magazine[r+1:]
        # return True
    
        '''
        App 2
        
        T.C - O(m)
        S.C - O(k) - for k unique chars
        '''
        if len(ransomNote) > len(magazine):
            return False

        magazine_counts = collections.Counter(magazine)
        ransom_note_counts = collections.Counter(ransomNote)

        for char, count in ransom_note_counts.items():
            magazine_count = magazine_counts[char]
            if magazine_count < count:
                return False

        
        return True