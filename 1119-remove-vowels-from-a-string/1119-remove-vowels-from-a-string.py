class Solution:
    def removeVowels(self, s: str) -> str:
        res=''
        for i in s:
            if i not in "aeiou":
                res+=i
        return res