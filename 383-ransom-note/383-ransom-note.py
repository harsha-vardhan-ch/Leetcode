class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in ransomNote:
            r=magazine.find(i)
            if r<0:
                return False
            else:
                magazine=magazine[:r]+magazine[r+1:]
        return True